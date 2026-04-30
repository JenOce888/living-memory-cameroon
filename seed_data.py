# seed_data.py — Populates the database with realistic sample data
# Run this ONCE with: python seed_data.py
# It simulates interviews with Cameroonian elders across different regions.

from app import create_app
from models import db
from models.person          import Person
from models.testimony       import Testimony
from models.oral_history    import OralHistory
from models.plant           import Plant
from models.medicinal_usage import MedicinalUsage
from datetime import date

app = create_app()

with app.app_context():

    # ── Clear existing data so we can run this script multiple times safely ──
    MedicinalUsage.query.delete()
    OralHistory.query.delete()
    Testimony.query.delete()
    Plant.query.delete()
    Person.query.delete()
    db.session.commit()
    print("Cleared existing data.")

    # ─────────────────────────────────────────────────────────────
    # PERSONS — elders from different regions and ethnic groups
    # ─────────────────────────────────────────────────────────────
    persons = [
        Person(last_name="Ngo Biyong",  first_name="Marguerite", approx_age=82,
               ethnic_group="Beti",       region="Centre",    city_village="Mbalmayo",
               native_language="Ewondo",  consent_given=True, interview_date=date(2026, 4, 1)),

        Person(last_name="Fomekong",    first_name="Emmanuel",  approx_age=76,
               ethnic_group="Bamiléké",   region="West",      city_village="Bafoussam",
               native_language="Ghomala",consent_given=True, interview_date=date(2026, 4, 3)),

        Person(last_name="Hamidou",     first_name="Oumarou",   approx_age=89,
               ethnic_group="Fulani",     region="Adamaoua",  city_village="Ngaoundéré",
               native_language="Fulfulde",consent_given=True, interview_date=date(2026, 4, 5)),

        Person(last_name="Essomba",     first_name="Célestine", approx_age=71,
               ethnic_group="Bassa",      region="Littoral",  city_village="Édéa",
               native_language="Bassa",   consent_given=True, interview_date=date(2026, 4, 7)),

        Person(last_name="Njoya",       first_name="Ibrahim",   approx_age=95,
               ethnic_group="Bamoun",     region="West",      city_village="Foumban",
               native_language="Bamoun",  consent_given=True, interview_date=date(2026, 4, 8)),

        Person(last_name="Mbarga",      first_name="Pierre",    approx_age=68,
               ethnic_group="Beti",       region="Centre",    city_village="Yaoundé",
               native_language="Ewondo",  consent_given=True, interview_date=date(2026, 4, 10)),

        Person(last_name="Abena",       first_name="Thérèse",   approx_age=74,
               ethnic_group="Bulu",       region="South",     city_village="Ebolowa",
               native_language="Bulu",    consent_given=True, interview_date=date(2026, 4, 12)),

        Person(last_name="Tagne",       first_name="Samuel",    approx_age=80,
               ethnic_group="Bamiléké",   region="West",      city_village="Dschang",
               native_language="Ghomala",consent_given=True, interview_date=date(2026, 4, 14)),

        Person(last_name="Manga",       first_name="Félicité",  approx_age=66,
               ethnic_group="Sawa",       region="Littoral",  city_village="Douala",
               native_language="Duala",   consent_given=True, interview_date=date(2026, 4, 15)),

        Person(last_name="Moussa",      first_name="Aïssatou",  approx_age=78,
               ethnic_group="Haoussa",    region="Far North", city_village="Maroua",
               native_language="Haoussa", consent_given=True, interview_date=date(2026, 4, 17)),
    ]

    for p in persons:
        db.session.add(p)
    db.session.flush()  # assigns IDs before we reference them below
    print(f"Added {len(persons)} persons.")

    # ─────────────────────────────────────────────────────────────
    # TESTIMONIES — historical events witnessed by the elders
    # ─────────────────────────────────────────────────────────────
    testimonies = [
        Testimony(
            person_id         = persons[0].id,
            title             = "The day independence was proclaimed in my village",
            transcription     = (
                "I was about 16 years old. My father came home running, shouting "
                "'We are free! Cameroon is independent!' We didn't fully understand "
                "what it meant, but everyone was dancing in the streets of Mbalmayo. "
                "The French administrator left the next week. We felt a great pride "
                "but also fear — what would happen next?"
            ),
            historical_period = "Independence (1960)",
            related_event     = "Cameroonian independence January 1st 1960",
            testimony_language= "French",
            record_date       = date(2026, 4, 1)
        ),
        Testimony(
            person_id         = persons[1].id,
            title             = "The economic crisis of 1990 and its effects on our family",
            transcription     = (
                "In 1990, civil servant salaries were cut by 50% overnight. My husband "
                "was a teacher — suddenly half his income disappeared. We had six children. "
                "We returned to farming to survive. The 'villes mortes' operations scared "
                "everyone. Shops closed, the streets were empty every Monday. "
                "It was a very dark period."
            ),
            historical_period = "1990s",
            related_event     = "Economic crisis and structural adjustment 1990",
            testimony_language= "French",
            record_date       = date(2026, 4, 3)
        ),
        Testimony(
            person_id         = persons[2].id,
            title             = "Life under the French administration in Ngaoundéré",
            transcription     = (
                "The French requisitioned our cattle for their army. We had no choice — "
                "if you refused, you were beaten or imprisoned. The chiefs who collaborated "
                "with them got favors. The others suffered. I saw my grandfather humiliated "
                "publicly by an administrator who was half his age."
            ),
            historical_period = "Colonial era (before 1960)",
            related_event     = "French colonial administration in northern Cameroon",
            testimony_language= "French",
            record_date       = date(2026, 4, 5)
        ),
        Testimony(
            person_id         = persons[3].id,
            title             = "The UPC war and the maquis near Édéa",
            transcription     = (
                "The Bassa region was at the heart of the resistance. At night we could "
                "hear gunshots. Ruben Um Nyobé was our hero — when he was killed in 1958, "
                "my mother cried for three days. The French soldiers would search our "
                "village looking for maquisards. Everyone was afraid. Some young men "
                "from our village joined the resistance and never came back."
            ),
            historical_period = "Colonial era (before 1960)",
            related_event     = "UPC uprising and Ruben Um Nyobé",
            testimony_language= "French",
            record_date       = date(2026, 4, 7)
        ),
        Testimony(
            person_id         = persons[4].id,
            title             = "The reunification of 1961 seen from Foumban",
            transcription     = (
                "We voted in the plebiscite. It was February 1961. In Foumban, most people "
                "wanted to join the French-speaking republic rather than Nigeria. Sultan "
                "Njoya's legacy made us feel culturally closer to the south. After the vote, "
                "there were celebrations but also confusion — two systems of government, "
                "two currencies at first, two sets of laws."
            ),
            historical_period = "Reunification (1961)",
            related_event     = "1961 plebiscite and reunification",
            testimony_language= "French",
            record_date       = date(2026, 4, 8)
        ),
        Testimony(
            person_id         = persons[5].id,
            title             = "Multiparty politics and the 1992 elections in Yaoundé",
            transcription     = (
                "In 1992 we believed change was possible. John Fru Ndi had huge support "
                "in Yaoundé too, not just the northwest. Election day there were long queues. "
                "Then the results were announced and people were furious. There were protests, "
                "the state of emergency was declared. Many young people lost hope that day "
                "and started thinking about leaving the country."
            ),
            historical_period = "1990s",
            related_event     = "1992 presidential elections",
            testimony_language= "French",
            record_date       = date(2026, 4, 10)
        ),
        Testimony(
            person_id         = persons[6].id,
            title             = "Schooling under colonial rule — the mission schools",
            transcription     = (
                "To go to school we walked 12 kilometers each way. The missionaries taught "
                "us to read in French and in Bulu. They forbade us from speaking our language "
                "in class — you would be beaten with a stick. But they also gave us books "
                "and opened our minds. It is a complicated memory."
            ),
            historical_period = "Colonial era (before 1960)",
            related_event     = "Mission schools and colonial education",
            testimony_language= "French",
            record_date       = date(2026, 4, 12)
        ),
        Testimony(
            person_id         = persons[7].id,
            title             = "The coffee boom of the 1970s in the West region",
            transcription     = (
                "The 1970s were good years. Coffee prices were high, the government "
                "supported farmers. My father built a concrete house with his coffee money. "
                "My brothers and I all went to secondary school. Then in the 1980s prices "
                "collapsed and everything became difficult again. But that decade of coffee "
                "prosperity changed our family's trajectory."
            ),
            historical_period = "1970s–1980s",
            related_event     = "Coffee economy and agricultural boom",
            testimony_language= "French",
            record_date       = date(2026, 4, 14)
        ),
        Testimony(
            person_id         = persons[8].id,
            title             = "Douala in the 1960s — the city of opportunities",
            transcription     = (
                "When I arrived in Douala in 1963 I was 18. The city was booming. "
                "The port was busy, there were factories opening, people from everywhere "
                "in Cameroon and from other African countries. It felt like anything was "
                "possible. I found work in a textile factory within one week. Today that "
                "factory is closed and the building is a ruin."
            ),
            historical_period = "Independence (1960)",
            related_event     = "Post-independence urban development Douala",
            testimony_language= "French",
            record_date       = date(2026, 4, 15)
        ),
        Testimony(
            person_id         = persons[9].id,
            title             = "Drought and famine in the Far North in the 1970s",
            transcription     = (
                "In 1973 the rains did not come. The sorghum dried in the fields. "
                "People walked days to find food. Children died in our village — I "
                "remember their names. International aid arrived months later, too late "
                "for many. The government did not respond quickly. That drought shaped "
                "how our community thinks about food security even today."
            ),
            historical_period = "1970s–1980s",
            related_event     = "Sahel drought and famine 1973",
            testimony_language= "French",
            record_date       = date(2026, 4, 17)
        ),
    ]

    for t in testimonies:
        db.session.add(t)
    print(f"Added {len(testimonies)} testimonies.")

    # ─────────────────────────────────────────────────────────────
    # ORAL HISTORIES — myths, proverbs, legends, folktales
    # ─────────────────────────────────────────────────────────────
    oral_histories = [
        OralHistory(
            person_id      = persons[0].id,
            category       = "proverb",
            title          = "Mfan a nga be ôba — The stranger does not own the tree",
            original_text  = "Mfan a nga be ôba, ôba a nga be mfan.",
            translation_fr = "L'étranger n'est pas l'arbre, l'arbre n'est pas l'étranger.",
            context        = (
                "This Ewondo proverb is used to remind guests to respect the customs "
                "of the house they visit. It is often said when a newcomer tries to "
                "impose his ways on an established community."
            ),
            ethnic_group   = "Beti",
            region         = "Centre",
            language       = "Ewondo",
            record_date    = date(2026, 4, 1)
        ),
        OralHistory(
            person_id      = persons[1].id,
            category       = "folktale",
            title          = "The spider and the chief's daughter",
            original_text  = "Kwi si a si fo fo sieh...",
            translation_fr = (
                "Il était une fois une araignée très rusée qui voulait épouser la fille "
                "du chef. Le chef posa trois défis impossibles. L'araignée réussit les "
                "deux premiers par ruse, mais au troisième défi elle fut piégée par sa "
                "propre vanité et perdit tout. La morale : la ruse sans sagesse mène à la chute."
            ),
            context        = (
                "This folktale is told to children in the evening around the fire. "
                "It teaches that cleverness alone is not enough — one must also have wisdom "
                "and humility. The spider is a common trickster figure in Bamiléké oral tradition."
            ),
            ethnic_group   = "Bamiléké",
            region         = "West",
            language       = "Ghomala",
            record_date    = date(2026, 4, 3)
        ),
        OralHistory(
            person_id      = persons[2].id,
            category       = "myth",
            title          = "The origin of the Fulani people and their cattle",
            original_text  = "Ko addi Fulaɓe e na'i...",
            translation_fr = (
                "Au commencement, Guéno le dieu créateur donna aux Peuls un troupeau "
                "de bœufs et leur dit : 'Prenez soin de ces animaux et ils prendront soin "
                "de vous.' Depuis ce jour les Peuls et leurs troupeaux sont inséparables. "
                "Celui qui maltraite son bétail offense Guéno lui-même."
            ),
            context        = (
                "This founding myth explains the sacred relationship between the Fulani "
                "people and their cattle. It is recited by elders during ceremonies related "
                "to livestock, marriages, and funerals. Only initiated elders may tell "
                "the complete version."
            ),
            ethnic_group   = "Fulani",
            region         = "Adamaoua",
            language       = "Fulfulde",
            record_date    = date(2026, 4, 5)
        ),
        OralHistory(
            person_id      = persons[3].id,
            category       = "legend",
            title          = "Ruben Um Nyobé — the man the forest protected",
            original_text  = "I ngui a Bassa...",
            translation_fr = (
                "On raconte que Ruben Um Nyobé connaissait tous les chemins de la forêt "
                "bassa. Les arbres le cachaient aux soldats français pendant des années. "
                "Les anciens disent que ce n'était pas de la chance — c'était parce qu'il "
                "avait fait un pacte avec les ancêtres pour protéger son peuple. Quand il "
                "fut trahi et tué, les feuilles des arbres tombèrent en pleine saison des pluies."
            ),
            context        = (
                "This semi-historical legend is told to keep the memory of the resistance alive. "
                "It blends real history with spiritual elements. Elders tell it to young people "
                "to teach courage and sacrifice for the community."
            ),
            ethnic_group   = "Bassa",
            region         = "Littoral",
            language       = "Bassa",
            record_date    = date(2026, 4, 7)
        ),
        OralHistory(
            person_id      = persons[4].id,
            category       = "tradition",
            title          = "The Nguon ceremony of the Bamoun kingdom",
            original_text  = "Nguon si a mbap...",
            translation_fr = (
                "Le Nguon est la grande fête du peuple Bamoun, célébrée tous les deux ans "
                "à Foumban. Le Sultan convoque tous les chefs de village. Chaque famille "
                "apporte des présents. On récite l'histoire du royaume, on juge les litiges, "
                "on célèbre les mariages royaux. Personne ne peut refuser l'invitation du Sultan."
            ),
            context        = (
                "The Nguon is one of the most important traditional institutions in Cameroon. "
                "It serves as a parliament, a court, and a cultural festival simultaneously. "
                "This elder is one of the few who remembers the ceremony before it was "
                "modernized in the 1980s."
            ),
            ethnic_group   = "Bamoun",
            region         = "West",
            language       = "Bamoun",
            record_date    = date(2026, 4, 8)
        ),
        OralHistory(
            person_id      = persons[6].id,
            category       = "proverb",
            title          = "Ngon a bulu — The woman is the root of the tree",
            original_text  = "Ngon a bulu, ngon a melan.",
            translation_fr = "La femme est la racine, la femme est la forêt.",
            context        = (
                "This Bulu proverb is used to honor the central role of women in the family "
                "and society. It is said at weddings and naming ceremonies. The elder explains "
                "that in Bulu culture, lineage passes through the mother's side."
            ),
            ethnic_group   = "Bulu",
            region         = "South",
            language       = "Bulu",
            record_date    = date(2026, 4, 12)
        ),
        OralHistory(
            person_id      = persons[9].id,
            category       = "myth",
            title          = "Why the baobab tree grows upside down",
            original_text  = "Tun baobab so a kai...",
            translation_fr = (
                "Au début du monde le baobab était l'arbre le plus orgueilleux. Il se "
                "vantait d'être plus grand que tous les autres. Dieu se fâcha et le "
                "replanta la tête en bas. Ses racines sont maintenant dans le ciel et "
                "ses branches dans la terre. C'est pourquoi le baobab ressemble à un "
                "arbre retourné — c'est sa punition pour l'orgueil."
            ),
            context        = (
                "This myth is told throughout the Sahel region including Far North Cameroon. "
                "It teaches children the danger of pride and arrogance. The baobab tree "
                "is considered sacred — one does not cut a baobab without asking permission "
                "from the ancestors."
            ),
            ethnic_group   = "Haoussa",
            region         = "Far North",
            language       = "Haoussa",
            record_date    = date(2026, 4, 17)
        ),
    ]

    for s in oral_histories:
        db.session.add(s)
    print(f"Added {len(oral_histories)} oral histories.")

    # ─────────────────────────────────────────────────────────────
    # PLANTS — medicinal plants with local names
    # ─────────────────────────────────────────────────────────────
    plants = [
        Plant(local_name="Joun Toū",       french_name="Roi des herbes",
              scientific_name="Vernonia amygdalina", botanical_family="Asteraceae",
              usage_region="West",    part_used="Leaves",
              description="Bitter shrub found at the edge of fields and forests. Leaves are very bitter. Known across sub-Saharan Africa.",
              record_date=date(2026, 4, 14) if hasattr(Plant, 'record_date') else None),

        Plant(local_name="Nkui",           french_name="Plante du veuvage",
              scientific_name="Triumfetta cordifolia", botanical_family="Tiliaceae",
              usage_region="West",    part_used="Leaves and stem",
              description="Climbing plant with sticky seeds. The leaves produce a thick mucilaginous soup. Used in post-partum and mourning ceremonies."),

        Plant(local_name="Atanga",         french_name="Safou / Prune d'Afrique",
              scientific_name="Dacryodes edulis", botanical_family="Burseraceae",
              usage_region="South",   part_used="Bark and fruit",
              description="Medium-sized tree producing purple-blue fruits. The bark is used medicinally, the fruit is eaten roasted."),

        Plant(local_name="Essok",          french_name="Feuille amère",
              scientific_name="Vernonia colorata", botanical_family="Asteraceae",
              usage_region="Centre",  part_used="Leaves",
              description="Wild shrub with dark green leaves. Related to Vernonia amygdalina. Used widely in Central region traditional medicine."),

        Plant(local_name="Owondo",         french_name="Moabi",
              scientific_name="Baillonella toxisperma", botanical_family="Sapotaceae",
              usage_region="South",   part_used="Bark and seeds",
              description="Large forest tree. The seeds produce moabi oil used in cooking and medicine. Sacred tree in many southern Cameroonian traditions."),

        Plant(local_name="Tchiayo",        french_name="Gingembre sauvage",
              scientific_name="Aframomum melegueta", botanical_family="Zingiberaceae",
              usage_region="Littoral", part_used="Roots and seeds",
              description="Wild ginger relative with spicy aromatic roots. Used in both cooking and traditional medicine across the Littoral region."),

        Plant(local_name="Kinkéliba",      french_name="Kinkéliba",
              scientific_name="Combretum micranthum", botanical_family="Combretaceae",
              usage_region="Far North", part_used="Leaves",
              description="Shrub found in Sahel zones. Leaves dried and used as herbal tea. Very common in northern Cameroon and across the Sahel."),

        Plant(local_name="Olom",           french_name="Plante du paludisme",
              scientific_name="Enantia chlorantha", botanical_family="Annonaceae",
              usage_region="Centre",  part_used="Bark",
              description="Small forest tree with yellow inner bark. The bark is intensely bitter due to alkaloids. Used specifically against malaria."),
    ]

    # Add record_date manually since it may not be in the model
    for p in plants:
        db.session.add(p)
    db.session.flush()
    print(f"Added {len(plants)} plants.")

    # ─────────────────────────────────────────────────────────────
    # MEDICINAL USAGES — who uses which plant for what
    # ─────────────────────────────────────────────────────────────
    usages = [
        MedicinalUsage(
            plant_id         = plants[0].id,  # Joun Toū
            person_id        = persons[1].id,  # Fomekong Emmanuel
            disease_treated  = "Malaria, fever, diabetes",
            preparation      = (
                "Boil a handful of fresh leaves in 1 liter of water for 15 minutes. "
                "Drink one cup morning and evening for 3 days. For diabetes: chew "
                "2-3 raw leaves every morning on an empty stomach."
            ),
            cultural_context = (
                "Called 'King of herbs' because it is believed to treat almost any illness. "
                "In Bamiléké tradition, the plant must be harvested before sunrise "
                "for maximum effectiveness. It is offered to guests as a sign of care."
            ),
            precautions      = "Very bitter — not recommended for young children or pregnant women in large doses."
        ),
        MedicinalUsage(
            plant_id         = plants[1].id,  # Nkui
            person_id        = persons[1].id,
            disease_treated  = "Post-partum recovery, strengthening new mothers",
            preparation      = (
                "Pound fresh leaves and stems. Mix with water and strain to obtain "
                "a thick dark green mucilaginous liquid. Add palm oil and spices. "
                "Served as a soup to new mothers every day for 40 days after childbirth."
            ),
            cultural_context = (
                "Nkui soup is a sacred post-partum tradition in Bamiléké culture. "
                "The mother-in-law is responsible for preparing it. Skipping this "
                "ritual is considered disrespectful to the newborn and the ancestors."
            ),
            precautions      = "Only for adult women. Not to be given to men or children."
        ),
        MedicinalUsage(
            plant_id         = plants[2].id,  # Atanga
            person_id        = persons[6].id,  # Abena Thérèse
            disease_treated  = "Skin infections, wounds, stomach pain",
            preparation      = (
                "For wounds: boil the bark, let it cool, wash the wound with the liquid "
                "twice a day. For stomach pain: dry the bark, grind into powder, "
                "dissolve one teaspoon in warm water, drink once a day."
            ),
            cultural_context = (
                "The Atanga tree is planted near houses in the South region as a protective "
                "spirit. One must greet the tree before harvesting its bark, otherwise "
                "the medicine will not work."
            ),
            precautions      = "Do not use the bark of a tree that has been struck by lightning."
        ),
        MedicinalUsage(
            plant_id         = plants[3].id,  # Essok
            person_id        = persons[0].id,  # Ngo Biyong Marguerite
            disease_treated  = "Malaria, high blood pressure",
            preparation      = (
                "Malaria: boil 10 fresh leaves in 500ml water for 10 minutes. "
                "Drink one cup three times a day for 5 days. "
                "Blood pressure: eat 2 raw leaves every morning for one month."
            ),
            cultural_context = (
                "In Beti tradition this plant is called 'the grandmother's medicine' "
                "because every grandmother knows how to use it. It is the first plant "
                "children learn about in traditional healing education."
            ),
            precautions      = "Do not combine with commercial anti-malaria drugs without consulting a healer."
        ),
        MedicinalUsage(
            plant_id         = plants[6].id,  # Kinkéliba
            person_id        = persons[9].id,  # Moussa Aïssatou
            disease_treated  = "Liver problems, digestive issues, general fatigue",
            preparation      = (
                "Dry the leaves in the shade for 3 days. Boil 2 tablespoons of dried "
                "leaves in 1 liter of water for 10 minutes. Drink as tea throughout the day, "
                "replacing water. Can be taken daily as a preventive tonic."
            ),
            cultural_context = (
                "Kinkéliba tea is drunk every morning in many Far North households. "
                "It is considered a daily health ritual, not just a medicine. "
                "Elders say those who drink it daily live longer and stay sharp-minded."
            ),
            precautions      = "Safe for daily consumption. Avoid during pregnancy in high quantities."
        ),
        MedicinalUsage(
            plant_id         = plants[7].id,  # Olom
            person_id        = persons[3].id,  # Essomba Célestine
            disease_treated  = "Malaria (severe cases)",
            preparation      = (
                "Scrape the inner yellow bark — the more yellow, the more potent. "
                "Boil 3 pieces (5cm each) in 2 liters of water for 20 minutes. "
                "Drink one large cup three times a day. The extreme bitterness means "
                "it is working. Treatment lasts 5 days."
            ),
            cultural_context = (
                "This tree is considered the most powerful anti-malaria plant in the "
                "Bassa tradition. Traditional healers guard the knowledge of correct "
                "dosage carefully — too much can be toxic. The healer must pray over "
                "the bark before giving it to the patient."
            ),
            precautions      = "Toxic in high doses. Must be prepared by someone trained. Not for children under 12."
        ),
    ]

    for u in usages:
        db.session.add(u)

    db.session.commit()
    print(f"Added {len(usages)} medicinal usages.")
    print("\n✅ Database seeded successfully!")
    print(f"   {len(persons)} persons | {len(testimonies)} testimonies | {len(oral_histories)} oral histories | {len(plants)} plants | {len(usages)} usages")
