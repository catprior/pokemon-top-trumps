<!-- PROJECT SHIELDS -->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]



<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/catprior/pokemon-top-trumps">
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/53/Poké_Ball_icon.svg/240px-Poké_Ball_icon.svg.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Pokemon Top Trumps</h3>

  <p align="center">
    A simple Pokemon Top Trumps game built using Flask.
    <br />
    <a href="https://github.com/catprior/pokemon-top-trumps"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/catprior/pokemon-top-trumps">View Demo</a>
    ·
    <a href="https://github.com/catprior/pokemon-top-trumps/issues">Report Bug</a>
    ·
    <a href="https://github.com/catprior/pokemon-top-trumps/issues">Request Feature</a>
  </p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary><h2 style="display: inline-block">Table of Contents</h2></summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a>
      <ul>
        <li><a href="#images">Images</a></li>
      </ul>
</li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

### Built With

* [Bootstrap](https://getbootstrap.com)
* [Flask](https://flask.palletsprojects.com)
* [PokeAPI](https://pokeapi.co)

<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

The following packages are required to run the game:
* Flask
  ```sh
  pip install flask
  ```
* Requests
  ```sh
  pip install requests
  ```
### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/catprior/pokemon-top-trumps.git
   ```
2. Install prerequisites
   ```sh
   pip install {package name}
   ```
3. Generate secret key
   ```sh
    python -c 'import os; print(os.urandom(16))'
   ```
3. Add secret key to `APP.SECRET_KEY` in `config.json`
   ```sh
    "APP.SECRET_KEY": "ADD YOUR SECRET KEY HERE"
   ```


<!-- ROADMAP -->
## Roadmap

See the [roadmap](https://github.com/catprior/pokemon-top-trumps/projects/1) for a list of proposed features (and known issues).



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



<!-- CONTACT -->
## Contact

Catherine Prior

Project Link: [https://github.com/catprior/pokemon-top-trumps](https://github.com/catprior/pokemon-top-trumps)



<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements

### Images
* [Pokemon (PokeAPI)](https://pokeapi.co)
* [Type Icons (Wikidata)](https://www.wikidata.org/wiki/Q1266830)
* [Pokeball (Wikidata)](https://www.wikidata.org/wiki/Q19847)



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/catprior/repo.svg?style=for-the-badge
[contributors-url]: https://github.com/catprior/pokemon-top-trumps/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/catprior/repo.svg?style=for-the-badge
[forks-url]: https://github.com/catprior/pokemon-top-trumps/network/members
[stars-shield]: https://img.shields.io/github/stars/catprior/repo.svg?style=for-the-badge
[stars-url]: https://github.com/catprior/pokemon-top-trumps/stargazers
[issues-shield]: https://img.shields.io/github/issues/catprior/repo.svg?style=for-the-badge
[issues-url]: https://github.com/catprior/pokemon-top-trumps/issues