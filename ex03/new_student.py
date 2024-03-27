import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    """
    generate id
    """
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    """
    dataclass
    """

    name: str = field(init=True)
    surname: str = field(init=True)
    active: bool = field(default=True)
    login: str = field(init=False, default="Eagle")
    id: str = field(init=False, default_factory=generate_id)

    def __post_init__(self):
        self.id = generate_id()


def main():
    student = Student(name="Edward", surname="agle")
    print(student)


if __name__ == "__main__":
    main()
