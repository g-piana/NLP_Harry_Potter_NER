<div id="top"></div>




<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

-->

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/github_username/repo_name">
    <img src="images/Harry_Potter_wordmark.gif" alt="Logo" width="218" heigth="74">
  </a>

<h3 align="center">Harry Potter | Humans and Myths</h3>

  <p align="center">
    Using the spaCy framework I developed a specialized dataset to train a NER model on custom entity recognition which I then rendered using Streamlit.
    <br />
    <a href="https://share.streamlit.io/g-piana/nlp_harry_potter_ner/main/08a_streamlit.py">View Demo</a>
    ·
    <a href="https://github.com/g-piana/nlp_harry_potter_ner/issues">Report Bug</a>
    ·
    <a href="https://github.com/g-piana/nlp_harry_potter_ner/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
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
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][Streamlit]](https://share.streamlit.io/g-piana/nlp_harry_potter_ner/main/08a_streamlit.py)

The purpose of this project is to test an end to end workflow from dataset preparation to deployment. As usual, most of the effort goes into creating a high quality dataset to train a custom model. However, the spaCy framework makes this type of efforts relatively smooth.

<p align="right">(<a href="#top">back to top</a>)</p>



### Built With

* [Python](https://python.org/)
* [spaCy](https://spacy.io/)
* [Streamlit](https://streamlit.io/)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

On the main root just issue:
  ```sh
streamlit run 08a_streamlit.py
  ```

It should open a local window in your browser.

### Prerequisites
I would recommend using a virtual environment. I like using Anaconda. 

* spacy_streamlit
  ```sh
  conda install -c conda-forge spacy-streamlit
  ```
* streamlit
  ```sh
  conda install -c conda-forge streamlit
  ```

### Installation

The model should run as it is. 

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage


<p align="right">(<a href="#top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [ ] Train the model on all books (currently it is trained on the first two books)
- [ ] Add additional mythological characters to labeling 
- [ ] Use this NLP functionality to develop document analysis


See the [open issues](https://github.com/g-piana/nlp_harry_potter_ner/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

[Giulio Piana](https://giuliopiana.com) - giuliopianaml@gmail.com

Project Link: [https://github.com/g-piana/nlp_harry_potter_ner](https://github.com/g-piana/nlp_harry_potter_ner)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* []()
* []()
* []()

<p align="right">(<a href="#top">back to top</a>)</p>



