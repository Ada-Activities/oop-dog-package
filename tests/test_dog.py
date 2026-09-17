from activity.dog import Dog

def test_dog_sits():
    dog = Dog("Fidough", 4)

    result = dog.sit()

    assert result == "Fidough is now sitting"


def test_dog_rolls_over():
    dog = Dog("Growlithe", 7)

    result = dog.roll_over()

    assert result == "Growlithe rolled over!"

