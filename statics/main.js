// main.js — small helpers used across all pages
// Nothing complex here — just a few utilities.

// Automatically hide success/error messages after 6 seconds
document.addEventListener('DOMContentLoaded', function() {
  document.querySelectorAll('.message:not(.hidden)').forEach(function(msg) {
    setTimeout(function() { msg.classList.add('hidden'); }, 6000);
  });
});
