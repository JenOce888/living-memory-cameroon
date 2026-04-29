# app.py — Main Flask application
# This file creates the app, registers all routes (pages + API endpoints),
# and connects everything together.

from flask import Flask, render_template, request, jsonify
from config import Config
from models import db
from models.person          import Person
from models.testimony       import Testimony
from models.oral_history    import OralHistory
from models.plant           import Plant
from models.medicinal_usage import MedicinalUsage
import cloudinary
import cloudinary.uploader
import pandas as pd


def create_app():
    """
    Factory function: creates and configures the Flask app.
    We use this pattern so the app can be tested easily.
    """
    app = Flask(__name__)
    app.config.from_object(Config)

    # Connect the database to the app
    db.init_app(app)

    # Configure Cloudinary (media file storage)
    cloudinary.config(
        cloud_name = app.config['CLOUDINARY_CLOUD_NAME'],
        api_key    = app.config['CLOUDINARY_API_KEY'],
        api_secret = app.config['CLOUDINARY_API_SECRET']
    )

    # Create all database tables if they don't exist yet
    with app.app_context():
        db.create_all()


    # ─────────────────────────────────────────────────────────────
    # PAGE ROUTES — these return HTML pages to the browser
    # ─────────────────────────────────────────────────────────────

    @app.route('/')
    def index():
        """Home page — shows a summary of what's in the database."""
        nb_persons       = Person.query.count()
        nb_testimonies   = Testimony.query.count()
        nb_oral_stories  = OralHistory.query.count()
        nb_plants        = Plant.query.count()
        return render_template('index.html',
            nb_persons      = nb_persons,
            nb_testimonies  = nb_testimonies,
            nb_oral_stories = nb_oral_stories,
            nb_plants       = nb_plants
        )

    @app.route('/collect-testimony')
    def collect_testimony():
        """Form to record a historical testimony from an elder."""
        return render_template('collect_testimony.html')

    @app.route('/collect-oral-history')
    def collect_oral_history():
        """Form to record a myth, legend, proverb, or folktale."""
        return render_template('collect_oral_history.html')

    @app.route('/collect-plant')
    def collect_plant():
        """Form to record a medicinal plant."""
        return render_template('collect_plant.html')

    @app.route('/browse')
    def browse():
        """Browse all collected records."""
        # Get the 'tab' parameter from the URL (e.g. /browse?tab=plants)
        tab = request.args.get('tab', 'testimonies')

        testimonies   = Testimony.query.order_by(Testimony.record_date.desc()).all()
        oral_histories= OralHistory.query.order_by(OralHistory.record_date.desc()).all()
        plants        = Plant.query.all()

        return render_template('browse.html',
            tab           = tab,
            testimonies   = testimonies,
            oral_histories= oral_histories,
            plants        = plants
        )

    @app.route('/dashboard')
    def dashboard():
        """Statistics page — charts and descriptive analysis."""
        return render_template('dashboard.html')


    # ─────────────────────────────────────────────────────────────
    # API ROUTES — these return JSON data (used by JavaScript)
    # ─────────────────────────────────────────────────────────────

    def upload_file(file, resource_type='auto', folder='cameroun_memory'):
        """
        Helper: uploads a file to Cloudinary and returns the public URL.
        Returns None if no file is provided or Cloudinary is not configured.
        """
        if not file or not file.filename:
            return None
        if not app.config['CLOUDINARY_CLOUD_NAME']:
            return None  # Cloudinary not configured (local dev)
        result = cloudinary.uploader.upload(file, resource_type=resource_type, folder=folder)
        return result.get('secure_url')


    @app.route('/api/testimony', methods=['POST'])
    def api_add_testimony():
        """
        API endpoint: receives the testimony form and saves to database.
        Handles both the Person (elder) and the Testimony records.
        """
        data  = request.form   # text fields
        files = request.files  # uploaded files

        # Step 1: Create the Person record
        person = Person(
            last_name       = data.get('last_name', ''),
            first_name      = data.get('first_name', ''),
            approx_age      = int(data['approx_age']) if data.get('approx_age') else None,
            ethnic_group    = data.get('ethnic_group', ''),
            region          = data.get('region', ''),
            city_village    = data.get('city_village', ''),
            native_language = data.get('native_language', ''),
            consent_given   = (data.get('consent_given') == 'on')
        )
        db.session.add(person)
        db.session.flush()  # flush so person.id is available before commit

        # Step 2: Upload audio file if provided
        audio_url = upload_file(files.get('audio'), resource_type='video', folder='cameroun_memory/audio')

        # Step 3: Create the Testimony record
        testimony = Testimony(
            person_id          = person.id,
            title              = data.get('title', ''),
            transcription      = data.get('transcription', ''),
            audio_url          = audio_url,
            historical_period  = data.get('historical_period', ''),
            related_event      = data.get('related_event', ''),
            testimony_language = data.get('testimony_language', '')
        )
        db.session.add(testimony)
        db.session.commit()

        return jsonify({'success': True, 'testimony_id': testimony.id, 'person_id': person.id})


    @app.route('/api/oral-history', methods=['POST'])
    def api_add_oral_history():
        """
        API endpoint: receives the oral history form and saves to database.
        An oral history can be a myth, legend, proverb, folktale, or tradition.
        """
        data  = request.form
        files = request.files

        # Step 1: Create or identify the person
        person = Person(
            last_name       = data.get('last_name', ''),
            first_name      = data.get('first_name', ''),
            approx_age      = int(data['approx_age']) if data.get('approx_age') else None,
            ethnic_group    = data.get('ethnic_group', ''),
            region          = data.get('region', ''),
            city_village    = data.get('city_village', ''),
            native_language = data.get('native_language', ''),
            consent_given   = (data.get('consent_given') == 'on')
        )
        db.session.add(person)
        db.session.flush()

        # Step 2: Upload audio if provided
        audio_url = upload_file(files.get('audio'), resource_type='video', folder='cameroun_memory/oral')

        # Step 3: Save the oral history
        story = OralHistory(
            person_id      = person.id,
            category       = data.get('category', 'other'),
            title          = data.get('title', ''),
            original_text  = data.get('original_text', ''),
            translation_fr = data.get('translation_fr', ''),
            context        = data.get('context', ''),
            ethnic_group   = data.get('ethnic_group', ''),
            region         = data.get('region', ''),
            language       = data.get('language', ''),
            audio_url      = audio_url
        )
        db.session.add(story)
        db.session.commit()

        return jsonify({'success': True, 'story_id': story.id})


    @app.route('/api/plant', methods=['POST'])
    def api_add_plant():
        """
        API endpoint: receives the plant form and saves to database.
        Also saves the medicinal usage if the elder described one.
        """
        data  = request.form
        files = request.files

        # Upload photo if provided
        photo_url = upload_file(files.get('photo'), resource_type='image', folder='cameroun_memory/plants')

        # Save the plant
        plant = Plant(
            local_name       = data.get('local_name', ''),
            french_name      = data.get('french_name', ''),
            scientific_name  = data.get('scientific_name', ''),
            botanical_family = data.get('botanical_family', ''),
            usage_region     = data.get('usage_region', ''),
            part_used        = data.get('part_used', ''),
            photo_url        = photo_url,
            description      = data.get('description', '')
        )
        db.session.add(plant)
        db.session.flush()

        # Save the medicinal usage if described
        if data.get('disease_treated') and data.get('person_id'):
            usage = MedicinalUsage(
                plant_id         = plant.id,
                person_id        = int(data['person_id']),
                disease_treated  = data.get('disease_treated', ''),
                preparation      = data.get('preparation', ''),
                cultural_context = data.get('cultural_context', ''),
                precautions      = data.get('precautions', '')
            )
            db.session.add(usage)

        db.session.commit()
        return jsonify({'success': True, 'plant_id': plant.id})


    @app.route('/api/stats')
    def api_stats():
        """
        API endpoint: returns descriptive statistics about all collected data.
        Used by the dashboard page to draw charts.
        """
        stats = {}

        # ── Person statistics ──
        persons = [p.to_dict() for p in Person.query.all()]
        stats['nb_persons'] = len(persons)

        if persons:
            df = pd.DataFrame(persons)

            # Age stats (ignore missing values with dropna)
            ages = df['approx_age'].dropna()
            if not ages.empty:
                stats['age'] = {
                    'mean':   round(ages.mean(), 1),
                    'min':    int(ages.min()),
                    'max':    int(ages.max()),
                    'median': round(ages.median(), 1)
                }

            # Count persons per region, ethnic group, language
            stats['by_region']        = df['region'].value_counts().to_dict()
            stats['by_ethnic_group']  = df['ethnic_group'].value_counts().to_dict()
            stats['by_language']      = df['native_language'].value_counts().to_dict()

        # ── Testimony statistics ──
        testimonies = [t.to_dict() for t in Testimony.query.all()]
        stats['nb_testimonies'] = len(testimonies)
        if testimonies:
            df_t = pd.DataFrame(testimonies)
            stats['testimonies_by_period'] = df_t['historical_period'].value_counts().to_dict()
            stats['testimonies_by_event']  = df_t['related_event'].value_counts().head(10).to_dict()

        # ── Oral history statistics ──
        stories = [s.to_dict() for s in OralHistory.query.all()]
        stats['nb_oral_stories'] = len(stories)
        if stories:
            df_s = pd.DataFrame(stories)
            stats['oral_by_category'] = df_s['category'].value_counts().to_dict()
            stats['oral_by_region']   = df_s['region'].value_counts().to_dict()
            stats['oral_by_language'] = df_s['language'].value_counts().to_dict()

        # ── Plant statistics ──
        plants = [p.to_dict() for p in Plant.query.all()]
        stats['nb_plants'] = len(plants)
        if plants:
            df_p = pd.DataFrame(plants)
            stats['plants_by_region']  = df_p['usage_region'].value_counts().to_dict()

        return jsonify(stats)


    @app.route('/api/search')
    def api_search():
        """
        API endpoint: full-text search across testimonies, oral histories, and plants.
        Usage: /api/search?q=leopard&type=oral
        """
        query = request.args.get('q', '').strip()
        type_ = request.args.get('type', 'testimony')  # testimony | oral | plant

        if not query:
            return jsonify([])

        if type_ == 'testimony':
            results = Testimony.query.filter(
                Testimony.title.ilike(f'%{query}%') |
                Testimony.transcription.ilike(f'%{query}%') |
                Testimony.related_event.ilike(f'%{query}%')
            ).limit(20).all()
            return jsonify([r.to_dict() for r in results])

        elif type_ == 'oral':
            results = OralHistory.query.filter(
                OralHistory.title.ilike(f'%{query}%') |
                OralHistory.original_text.ilike(f'%{query}%') |
                OralHistory.translation_fr.ilike(f'%{query}%') |
                OralHistory.context.ilike(f'%{query}%')
            ).limit(20).all()
            return jsonify([r.to_dict() for r in results])

        else:  # plant
            results = Plant.query.filter(
                Plant.local_name.ilike(f'%{query}%') |
                Plant.french_name.ilike(f'%{query}%') |
                Plant.description.ilike(f'%{query}%')
            ).limit(20).all()
            return jsonify([r.to_dict() for r in results])


    return app


# ─────────────────────────────────────────────────────────────
# Entry point — runs when you do: python app.py
# ─────────────────────────────────────────────────────────────
app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
