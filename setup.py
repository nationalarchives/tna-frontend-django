import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="nationalarchives-frontend-django",
    version="0.1.1-alpha",
    author="Andrew Hosgood",
    author_email="andrew.hosgood@nationalarchives.gov.uk",
    description="The National Archives frontend Django templates",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/nationalarchives/tna-frontend-django",
    project_urls={
        "Bug Tracker": "https://github.com/nationalarchives/tna-frontend-django/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Code Generators",
        "Topic :: Software Development :: User Interfaces",
        "Topic :: Text Processing :: Markup :: HTML",
    ],
    packages=setuptools.find_packages(exclude=["django", "components"]),
    package_data={
        "nationalarchives-frontend-django.templates.components": ["*.html"],
    },
    python_requires=">=3.8",
    install_requires=["Django>=4"],
)
