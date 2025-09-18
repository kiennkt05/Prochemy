from setuptools import setup, find_packages

setup(
    name="human-eval",
    version="1.0.1",  # Slightly higher version to override the global one
    author="OpenAI",
    description="Human Eval - Windows Compatible Version",
    packages=find_packages(),
    install_requires=[
        "fire",
        "numpy",
        "tqdm",
    ],
    entry_points={
        'console_scripts': [
            'evaluate_functional_correctness=human_eval.evaluate_functional_correctness:main',
        ],
    },
    python_requires='>=3.6',
)
