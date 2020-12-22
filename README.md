# MNIST Sandbox

## Description

A basic multilayer perceptron wrapped in a Tkinter GUI which
allows users to train it on the MNIST handwritten digit dataset with a custom batch size, number of epochs, and training rate. Then, you can drawing draw your own digits and query them on the model.

## Installation

1. Clone this repository.

   ```bash
   git clone https://github.com/jkatofsky/MNIST-sandbox.git
   ```

2. Install the required modules.

   ```bash
   pip3 install -r requirements.txt
   ```

3. Run the sandbox! It will take longer than usual on the first launch as it downloads the training data.

   ```bash
   python3 App.py
   ```

## TODOs

I'm continually revisiting this project and making improvements!

- [x] A proper README
- [x] A proper installation process such that anyone can run the repo locally (w/ automatic training data download)
  - [ ] A _better_ installation process: GUI should prompt for OK to download training data & display progress indicator. Also figure out the best way to distribute more generally; it's sort of like a Python module right now.
- [ ] Change dataset to [EMNIST?](https://www.nist.gov/itl/products-and-services/emnist-dataset)
- [ ] The predictions for drawn digits are still finnicky and not as accurate as the training dataset; investigate this
- [ ] GUI responsivity - scroll bars, pop-ups for errors, loading bars
- [ ] Better seperation of concerns between GUI and logic
- [ ] Revisit directory structure
