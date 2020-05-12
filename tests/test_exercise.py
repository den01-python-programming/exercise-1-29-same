import pytest
import src.exercise

def test_exercise():
    input_values = ["Bridgend","Bridgend","Pencoed","Bridgend"]
    input_values_stored = ["Bridgend","Bridgend","Pencoed","Bridgend"]
    output = []

    def mock_input(s=None):
        if s is not None:
            output.append(s)
            return input_values.pop(0)
        else:
            output.append("")
            return input_values.pop(0)

    src.exercise.input = mock_input
    src.exercise.print = lambda s : output.append(s)

    src.exercise.main()

    src.exercise.input = mock_input
    src.exercise.print = lambda s : output.append(s)

    src.exercise.main()

    assert [output[0],output[1],output[2]] == ["Enter the first string:",\
                                               "Enter the second string:",\
                                               "Same"]
    assert [output[3],output[4],output[5]] == ["Enter the first string:",\
                                              "Enter the second string:",\
                                              "Different"]
