from pytest import mark, raises

from raksh.result import (
    auto,
    FailureCode,
    GenericFailureCode,
    GenericSuccessCode,
    SuccessCode,
)


class TestFailureCode:

    def test_str_Returns_title_case_With_underscores_converted_to_spaces(self):
        class FakeFailureCode(FailureCode):
            HELLO_WORLD = 1
            FOO = 2
            bAR_BaZ = 3

        assert str(FakeFailureCode.HELLO_WORLD) == "Hello World"
        assert str(FakeFailureCode.FOO) == "Foo"
        assert str(FakeFailureCode.bAR_BaZ) == "Bar Baz"

    def test_Respects_manually_defined_value_When_non_zero(self):
        class FakeFailureCode(FailureCode):
            BAR = 1
            BAZ = -1

        class FakeFailureCodeTuple(FailureCode):
            BAR = "1a", 16
            BAZ = "11", 8

        assert FakeFailureCode.BAR == 1
        assert FakeFailureCode.BAZ == -1

        assert FakeFailureCodeTuple.BAR == 26
        assert FakeFailureCodeTuple.BAZ == 9

    def test_auto_Generates_incremental_values_From_1_When_auto_used(self):
        class FakeFailureCode(FailureCode):
            FOO = auto()
            BAR = 100
            BAZ = auto()

        assert FakeFailureCode.FOO == 1
        assert FakeFailureCode.BAZ == 101

    def test_auto_Generates_incremental_values_From_last_defined_value(self):
        class FakeFailureCode(FailureCode):
            FOO = -3
            BAR = auto()
            BAZ = 5
            QUX = auto()

        class FakeFailureCodeTuple(FailureCode):
            FOO = "-1a", 16
            BAR = auto()
            BAZ = "1a", 16
            QUX = auto()

        assert FakeFailureCode.BAR == -2
        assert FakeFailureCode.QUX == 6
        assert FakeFailureCodeTuple.BAR == -25
        assert FakeFailureCodeTuple.QUX == 27

    def test_auto_Handles_negative_To_positive_increment(self):
        class FakeFailureCodeInt(FailureCode):
            FOO = -1
            BAR = auto()
            BAZ = auto()

        assert int(FakeFailureCodeInt.BAR) == 1
        assert int(FakeFailureCodeInt.BAZ) == 2

    def test_Raises_value_error_When_zero_value_defined(self):

        with raises(ValueError):

            class _(FailureCode):
                FOO = 0


class TestGenericFailureCode:

    @mark.parametrize(
        "code, s",
        [
            (GenericFailureCode.FAILURE, "Failure"),
            (
                GenericFailureCode.UNEXPECTED_EXCEPTION_RAISED,
                "Unexpected Exception Raised",
            ),
        ],
    )
    def test_str_Returns_expected_value(self, code: GenericFailureCode, s: str):
        assert str(code) == s

    @mark.parametrize(
        "code",
        [GenericFailureCode.FAILURE, GenericFailureCode.UNEXPECTED_EXCEPTION_RAISED],
    )
    def test_Not_equal_to_zero(self, code: GenericFailureCode):
        assert code != 0


class TestGenericSuccessCode:

    @mark.parametrize(
        "code, s",
        [
            (GenericSuccessCode.NO_OPERATION, "No Operation"),
            (GenericSuccessCode.SUCCESS, "Success"),
        ],
    )
    def test_str_Returns_expected_value(self, code: GenericSuccessCode, s: str):
        assert str(code) == s

    @mark.parametrize(
        "code",
        [GenericSuccessCode.NO_OPERATION, GenericSuccessCode.SUCCESS],
    )
    def test_Equals_zero(self, code: GenericFailureCode):
        assert code == 0


class TestSuccessCode:

    def test_str_Returns_title_case_With_underscores_converted_to_spaces(self):
        class FakeSuccessCode(SuccessCode):
            HELLO_WORLD = 0
            FOO = 0
            bAR_BaZ = 0

        assert str(FakeSuccessCode.HELLO_WORLD) == "Hello World"
        assert str(FakeSuccessCode.FOO) == "Foo"
        assert str(FakeSuccessCode.bAR_BaZ) == "Bar Baz"

    def test_is_Returns_true_When_comparing_same_member(self):
        class FakeSuccessCode(SuccessCode):
            FOO = 0
            BAR = 0

        assert FakeSuccessCode.FOO is FakeSuccessCode.FOO

    def test_is_Returns_false_When_comparing_different_members(self):
        class FakeSuccessCode(SuccessCode):
            FOO = 0
            BAR = 0

        assert FakeSuccessCode.FOO is not FakeSuccessCode.BAR

    def test_auto_Returns_zero(self):
        class FakeSuccessCode(SuccessCode):
            FOO = auto()
            BAR = auto()

        assert FakeSuccessCode.FOO == 0
        assert FakeSuccessCode.BAR == 0

    def test_Raises_value_error_When_non_zero_value_provided(self):
        with raises(ValueError):

            class _(SuccessCode):
                FOO = 1
