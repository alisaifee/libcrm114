import tempfile
import unittest
import pycrm114
from pycrm114.storage.fs import FileSystemStorage


class SmokeTests(unittest.TestCase):
    def test_basic_initialization(self):
        crm = pycrm114.CRM114(["spam", "ham"])
        crm.learn("spam", "buy viagra")
        crm.learn("ham", "hi there")
        self.assertEqual(crm.classify("would you like to buy viagra")['class'], 'spam')

    def test_custom_flags(self):
        crm = pycrm114.CRM114(["spam", "ham"], flags=pycrm114.flags.CRM114_MICROGROOM)
        crm.learn("spam", "buy viagra")
        crm.learn("ham", "hi there")
        self.assertEqual(crm.classify("would you like to buy viagra")['class'], 'spam')

    def test_basic_persistence(self):
        temp_dir = tempfile.mkdtemp()
        crm = pycrm114.CRM114(["spam", "ham"], storage=FileSystemStorage(temp_dir), auto_save=True)
        crm.learn("spam", "buy viagra")
        crm.learn("ham", "hi there")
        self.assertEqual(crm.classify("would you like to buy viagra")['class'], 'spam')
        new_crm = pycrm114.CRM114(["spam", "ham"], storage=FileSystemStorage(temp_dir), auto_save=True)
        self.assertEqual(new_crm.classify("would you like to buy viagra")['class'], 'spam')

    def test_unlearn(self):
        crm = pycrm114.CRM114(["spam", "ham"])
        self.assertTrue(crm.classify("is spam good")['score']==0.5)
        crm.learn("spam", "spam is good")
        self.assertTrue(crm.classify("is spam good")['score']>0.5)
        crm.forget("spam", "spam is good")
        self.assertTrue(crm.classify("is spam good")['score']==0.5)
        crm.learn("spam", "spam is good")
        self.assertTrue(crm.classify("is spam good")['score']>0.5)
