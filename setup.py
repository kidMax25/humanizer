from setuptools import setup, find_packages

setup(
    name="gemini-rewriter",
    version="1.0.0",
    description="Text rewriting tool using Google's Gemini AI",
    author="Your Name",
    packages=find_packages(),
    install_requires=[
        "google-generativeai>=0.3.0",
        "asyncio",
        "logging",
        "typing",
    ],
    entry_points={
        "console_scripts": [
            "gemini-rewrite=gemini_rewriter.gemini_rewriter:main"
        ]
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    python_requires=">=3.7",
)