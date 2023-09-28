# Single Error Correction App Documentation

Welcome to the Single Error Correction App documentation. This app is designed to implement the single error detection algorithm in python with graphical user interface built with Pyside6.

# Installation

To install the Single Error Correction App, follow these steps:

1. Clone the repository from Github:
   git clone https://github.com/DamaMichaelYohanna/single-error-correction.git

2. Navigate to the project directory:
   cd single-error-correction

3. Install the required dependencies
   pip install Pyside6

# Usage

## Running the App

To run the app, open your terminal/command prompt from the the project folder. and execute the following command:
python interface.py

## Using the GUI

1. Once you run, the command above, you will be provided with a graphical user interface with input area to enalble you type in the word to generated equivalent hamming code.

2. After step one above, you will be taken to the second screen where you can type in an erronous codeword. On submitting, the program automatically detect if the codeword contains error. if it does, it give you the position of the error, the index, and the parity bits. The program isn't at it best as it can only detect single error.

# Features

- Generate Hamming Code:
  The program is able to generate hamming code for any given length of data.

- Single Error Detection:
  The program is able to detect single errors, providing the index, position and bit value.

- User-Friendly Interface
  A Graphical user interface built with Pyside6 in python for easy interation

# Troubleshooting

## Common Issues

1. Issue 1: Wrong python installation. Without a proper python installation, you won't be able to install the needed packages to enable you run the program.

2. Issue 2: Wrong package installation. There are several UI package out there, but in our case, we used pyside version 6. Note: This program was not tested on a lower version of pyside.
