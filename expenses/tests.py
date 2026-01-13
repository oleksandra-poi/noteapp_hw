from django.test import TestCase
from django.urls import reverse
from .models import Note, Category
from datetime import date

class NoteTests(TestCase):

    def setUp(self):
        self.category = Category.objects.create(title="Work")

        self.note = Note.objects.create(
            title="Test Note",
            text="Test content",
            reminder=date.today(),
            category=self.category
        )

    def test_note_creation(self):
        """Test that a note is created correctly"""
        self.assertEqual(Note.objects.count(), 1)
        self.assertEqual(self.note.title, "Test Note")

    def test_note_update(self):
        """Test updating a note"""
        self.note.title = "Updated Title"
        self.note.save()

        updated_note = Note.objects.get(id=self.note.id)
        self.assertEqual(updated_note.title, "Updated Title")

    def test_note_delete(self):
        """Test deleting a note"""
        self.note.delete()
        self.assertEqual(Note.objects.count(), 0)

    def test_home_page_status_code(self):
        """Home page loads correctly"""
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_note_displayed_on_home_page(self):
        """Note is shown on home page"""
        response = self.client.get(reverse('home'))
        self.assertContains(response, "Test Note")
