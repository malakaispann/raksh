from raksh.result import (
    FailureCode,
    GenericFailureCode,
    GenericSuccessCode,
    Result,
    SuccessCode,
)


class TestResult:

    def test_success_Creates_result_With_expected_defaults(self):
        result = Result.success()
        assert result.code is GenericSuccessCode.SUCCESS
        assert result.value is None

    def test_success_Creates_result_With_provided_code_and_value(
        self,
    ):
        class FakeSuccessCode(SuccessCode):
            FOO = 0
            BAR = 0
            BAZ = 0

        value = "foo"
        code = FakeSuccessCode.BAZ

        result = Result.success(value, code)
        assert result.value == value
        assert result.code is code

    def test_failure_Creates_result_With_expected_defaults(
        self,
    ):
        result = Result.failure()
        assert result.code is GenericFailureCode.FAILURE
        assert result.value is None

    def test_failure_Creates_result_With_provided_code_and_value(
        self,
    ):
        class FakeFailureCode(FailureCode):
            FOO = 1
            BAR = 2
            BAZ = 3

        value = "foo"
        code = FakeFailureCode.BAR

        result = Result.failure(code, value)
        assert result.code is code
        assert result.value == value

    def test_is_success_Returns_true_When_success_code_used(self):
        assert Result(GenericSuccessCode.SUCCESS).is_success

    def test_is_failure_Returns_false_When_success_code_used(self):
        assert not Result(GenericSuccessCode.SUCCESS).is_failure

    def test_is_success_Returns_false_When_failure_code_used(self):
        assert not Result(GenericFailureCode.FAILURE).is_success

    def test_is_failure_Returns_true_When_failure_code_used(self):
        assert Result(GenericFailureCode.FAILURE).is_failure

    def test_str_Returns_formatted_representation(
        self,
    ):
        class CustomFailureCode(FailureCode):
            NETWORK_ERROR = 1

        assert (
            str(Result.failure(CustomFailureCode.NETWORK_ERROR))
            == "(CustomFailureCode) Network Error"
        )
