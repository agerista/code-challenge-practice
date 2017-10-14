class FormField(object):
    def __init__(self, title, help_text=None):
        self.title = title
        self.help_text = help_text

    def submit_answer(self, answer):
        return self.answer

    def get_answer(self):
        pass

    def is_valid(self):
        raise NotImplementedError()


class TextField(FormField):
    def submit_answer(self, answer):
        pass

    def get_answer(self):
        pass

    


class EmailField(FormField):
    pass


class URLField(FormField):
    pass


class MultipleChoiceField(FormField):
    def __init__(self, title, options, help_text=None):
        pass

#######################################################################
if __name__ == "__main__":
    import pytest

    text_field = TextField(
        "What do you like about RMOTR?",
        help_text="Mentors? Classes? Assignments?")
    print(text_field.help_text)  # "Mentors? Classes? Assignments?"

    text_field.is_valid()  # WARNING! Raises ValueError

    text_field.submit_answer('Mentoring!')

    text_field.is_valid()  # True

    def test_multiple_choice_field_is_valid():
        multi_field = MultipleChoiceField(
            "What's your preferred language?",
            ['Python', 'Ruby', 'Javascript'],
            help_text="There's only one correct answer ;)")

        multi_field.submit_answer('Python')
        assert multi_field.is_valid()

        assert multi_field.help_text == "There's only one correct answer ;)"

    def test_url_field_is_valid():
        twitter_field = URLField("Twitter profile URL?")
        twitter_field.submit_answer('https://twitter.com/rmotr_com')
        assert twitter_field.is_valid()

    def test_url_form_field_unbound():
        twitter_field = URLField("Twitter profile URL?")

        with pytest.raises(ValueError):
            twitter_field.is_valid()

    def test_email_field_is_valid():
        email_field = EmailField("What's your email?")
        email_field.submit_answer('questions@rmotr.com')
        assert email_field.is_valid()

    def test_email_form_field_unbound():
        email_field = EmailField("What's your email?")

        with pytest.raises(ValueError):
            email_field.is_valid()

    def test_email_field_is_invalid():
        email_field = EmailField("What's your email?")
        email_field.submit_answer('INVALID EMAIL')
        assert not email_field.is_valid()

    def test_text_form_field_unbound():
        text_field = TextField(
            "What do you like about RMOTR?",
            help_text="Mentors? Classes? Assignments?")

        with pytest.raises(ValueError):
            text_field.is_valid()

        assert text_field.help_text == "Mentors? Classes? Assignments?"

    def test_url_field_is_invalid():
        twitter_field = URLField("Twitter profile URL?")
        twitter_field.submit_answer('INVALID URL')

        assert not twitter_field.is_valid()

    def test_multiple_choice_form_field_unbound():
        multi_field = MultipleChoiceField(
            "What's your preferred language?",
            ['Python', 'Ruby', 'Javascript'],
            help_text="There's only one correct answer ;)")

        with pytest.raises(ValueError):
            multi_field.is_valid()

        assert multi_field.help_text == "There's only one correct answer ;)"

    def test_text_form_fields():
        text_field = TextField(
            "What do you like about RMOTR?",
            help_text="Mentors? Classes? Assignments?")

        text_field.submit_answer('Mentoring, for sure!')

        assert text_field.is_valid()

    def test_multiple_choice_field_invalid():
        multi_field = MultipleChoiceField(
            "What's your preferred language?",
            ['Python', 'Ruby', 'Javascript'])

        multi_field.submit_answer('Invalid Language')
        assert not multi_field.is_valid()
