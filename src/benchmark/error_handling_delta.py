#!/usr/bin/env python3
"""Benchmarks comparing exception handling vs result-based error handling."""

import statistics
import time
from typing import Tuple

from raksh.result import FailureCode, Result, SuccessCode, auto


__all__ = [
    "BenchmarkError",
    "BenchmarkFailureCode",
    "BenchmarkSuccessCode",
    "benchmark_function",
    "commander_exception",
    "commander_result",
    "run_benchmarks",
    "worker_exception",
    "worker_result",
]


class BenchmarkError(Exception):
    """Custom exception for benchmark error cases."""


class BenchmarkFailureCode(FailureCode):
    """Failure codes for benchmark operations."""

    OPERATION_FAILED = auto()


class BenchmarkSuccessCode(SuccessCode):
    """Success codes for benchmark operations."""

    OPERATION_SUCCEEDED = auto()


def worker_exception(should_fail: bool) -> int:
    """Worker function that uses exceptions for error handling.

    Args:
        should_fail: Whether to trigger error case.

    Returns:
        Fixed integer value on success.

    Raises:
        BenchmarkError: When should_fail is True.
    """
    if should_fail:
        raise BenchmarkError("Operation failed")
    return 42


def worker_result(should_fail: bool) -> Result[int]:
    """Worker function that uses Result for error handling.

    Args:
        should_fail: Whether to trigger error case.

    Returns:
        Result containing success or failure state.
    """
    if should_fail:
        return Result.failure(code=BenchmarkFailureCode.OPERATION_FAILED, value=None)
    return Result.success(value=42, code=BenchmarkSuccessCode.OPERATION_SUCCEEDED)


def commander_exception(should_fail: bool) -> int:
    """Commander that handles worker_exception errors.

    Args:
        should_fail: Whether to trigger error case.

    Returns:
        Worker return value on success, -1 on error.
    """
    try:
        return worker_exception(should_fail)
    except BenchmarkError:
        return -1


def commander_result(should_fail: bool) -> int:
    """Commander that handles worker_result errors.

    Args:
        should_fail: Whether to trigger error case.

    Returns:
        Worker return value on success, -1 on error.
    """
    result = worker_result(should_fail)
    if result.is_failure:
        return -1
    return result.value


def benchmark_function(
    func, should_fail: bool, iterations: int = 1_000_000
) -> Tuple[float, float]:
    """Benchmarks a function multiple times and returns timing statistics.

    Args:
        func: Function to benchmark.
        should_fail: Argument to pass to function.
        iterations: Total number of iterations to run.

    Returns:
        Tuple of (mean_time_ms, std_deviation_ms).
    """
    times = []
    iterations_per_run = iterations // 10

    for _ in range(10):
        start = time.perf_counter_ns()
        for _ in range(iterations_per_run):
            func(should_fail)
        end = time.perf_counter_ns()
        times.append((end - start) / 1_000_000)  # Convert to ms

    mean_time = statistics.mean(times)
    std_dev = statistics.stdev(times)
    return mean_time, std_dev


def run_benchmarks():
    """Runs benchmarks comparing exception and result-based error handling."""
    iterations = 1_000_000
    print(f"Running benchmarks with {iterations:,} iterations each...\n")

    print("=" * 60)
    print("BENCHMARK 1: Error case (should_fail=True)")
    print("=" * 60)

    exception_time, exception_std = benchmark_function(
        commander_exception, True, iterations
    )
    result_time, result_std = benchmark_function(commander_result, True, iterations)

    print(f"Exception approach: {exception_time:.2f} ms (±{exception_std:.2f} ms)")
    print(f"Result approach:    {result_time:.2f} ms (±{result_std:.2f} ms)")
    print(f"Difference:         {abs(exception_time - result_time):.2f} ms")
    print(
        f"Ratio:              "
        f"{max(exception_time, result_time) / min(exception_time, result_time):.2f}x"
    )

    print("\n" + "=" * 60)
    print("BENCHMARK 2: Success case (should_fail=False)")
    print("=" * 60)

    exception_time_success, exception_std_success = benchmark_function(
        commander_exception, False, iterations
    )
    result_time_success, result_std_success = benchmark_function(
        commander_result, False, iterations
    )

    print(
        f"Exception approach: {exception_time_success:.2f} ms "
        f"(±{exception_std_success:.2f} ms)"
    )
    print(
        f"Result approach:    {result_time_success:.2f} ms "
        f"(±{result_std_success:.2f} ms)"
    )
    print(
        f"Difference:         "
        f"{abs(exception_time_success - result_time_success):.2f} ms"
    )
    print(
        f"Ratio:              "
        f"{max(exception_time_success, result_time_success) / min(exception_time_success, result_time_success):.2f}x"
    )

    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print(
        f"Error case overhead (Exception vs Result): "
        f"{exception_time / result_time:.2f}x"
    )
    print(
        f"Success case overhead (Result vs Exception): "
        f"{result_time_success / exception_time_success:.2f}x"
    )


if __name__ == "__main__":
    run_benchmarks()
