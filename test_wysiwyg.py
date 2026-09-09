import pathlib
import unittest

HTML = pathlib.Path(__file__).with_name("index.html").read_text()


class WysiwygEditorTest(unittest.TestCase):
    def test_toolbar_has_core_formatting_controls(self):
        for command in ("bold", "italic", "insertUnorderedList", "undo", "redo", "removeFormat"):
            self.assertIn(f"runCommand('{command}')", HTML)

    def test_edits_are_saved_locally(self):
        self.assertIn("const STORAGE_KEY", HTML)
        self.assertIn("localStorage.setItem(STORAGE_KEY", HTML)
        self.assertIn("restoreLocalDraft()", HTML)

    def test_save_state_is_visible(self):
        self.assertIn('id="saveStatus"', HTML)
        self.assertIn("function setSaveStatus", HTML)


if __name__ == "__main__":
    unittest.main()
