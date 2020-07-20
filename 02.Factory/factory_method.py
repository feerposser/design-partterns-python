from abc import ABCMeta, abstractmethod


class Section(metaclass=ABCMeta):
    @abstractmethod
    def describe(self):
        pass


class PersonalSection(Section):
    def describe(self):
        print("Personal section")


class AlbumSection(Section):
    def describe(self):
        print("Album section")


class PatentSection(Section):
    def describe(self):
        print("Patent section")


class PublicationSection(Section):
    def describe(self):
        print("Publication section")


# ------------------------------------------


class Profile(metaclass=ABCMeta):
    def __init__(self):
        self.sections = []
        self.create_profile()

    @abstractmethod
    def create_profile(self):
        pass

    def get_sections(self):
        return self.sections

    def add_sections(self, section):
        self.sections.append(section)


class Facebook(Profile):
    def create_profile(self):
        self.add_sections(PersonalSection())
        self.add_sections(AlbumSection())


class LinedIn(Profile):
    def create_profile(self):
        self.add_sections(PersonalSection())
        self.add_sections(PublicationSection())
        self.add_sections(PatentSection())


if __name__ == "__main__":
    profile_type = input("Facebook ou LinkedIn? ")
    profile = eval(profile_type)()
    print("Criando: ", type(profile).__name__)
    print("Seções:\n", profile.get_sections())

