# musicAI: Music Generation for Multiple Genres and Novel Sampling Techniques with Transformer-XL

Adapted from: REMI
Authors: [Yu-Siang Huang](https://remyhuang.github.io/), [Yi-Hsuan Yang](http://mac.citi.sinica.edu.tw/~yang/)

[**Paper (arXiv)**](https://arxiv.org/abs/2002.00212) | [**Blog**](https://ailabs.tw/human-interaction/pop-music-transformer/) | [**Audio demo (Google Drive)**](https://drive.google.com/open?id=1LzPBjHPip4S0CBOLquk5CNapvXSfys54) | [**Online interactive demo**](https://vibertthio.com/transformer/)

## Getting Started
### Install Dependencies
* python 3.6 (recommend using [Anaconda](https://www.anaconda.com/distribution/))
* tensorflow-gpu 1.14.0 (`pip install tensorflow-gpu==1.14.0`)
* [miditoolkit](https://github.com/YatingMusic/miditoolkit) (`pip install miditoolkit`)

### Download Pre-trained Checkpoints
We provide two pre-trained checkpoints for generating samples.
* `REMI-tempo-checkpoint` [(428 MB)](https://drive.google.com/open?id=1gxuTSkF51NP04JZgTE46Pg4KQsbHQKGo)
* `REMI-tempo-chord-checkpoint` [(429 MB)](https://drive.google.com/open?id=1nAKjaeahlzpVAX0F9wjQEG_hL4UosSbo)

### Obtain the MIDI Data
We provide the MIDI files including local tempo changes and estimated chord. [(5 MB)](https://drive.google.com/open?id=1JUDHGrVYGyHtjkfI2vgR1xb2oU8unlI3)
* `data/train`: 775 files used for training models
* `data/evaluation`: 100 files (prompts) used for the continuation experiments

## Generate Samples
A generation script is provided as generate_script.py, see source code for command flags.
Example usage:
```
python generate_script.py --nb 32
```
## Convert MIDI to REMI
You can find out how to convert the MIDI messages into REMI events in the `midi2remi.ipynb`.

## FAQ
#### 1. How to synthesize the audio files (e.g., mp3)?
We strongly recommend using DAW (e.g., Logic Pro) to open/play the generated MIDI files. Or, you can use [FluidSynth](https://github.com/FluidSynth/fluidsynth) with a [SoundFont](https://sites.google.com/site/soundfonts4u/). However, it may not be able to correctly handle the tempo changes (see [fluidsynth/issues/141](https://github.com/FluidSynth/fluidsynth/issues/141)).

#### 2. What is the function of the inputs "temperature" and "topk"?
It is the temperature-controlled stochastic sampling methods are used for generating text from a trained language model. You can find out more details in the reference paper [CTRL: 4.1 Sampling](https://einstein.ai/presentations/ctrl.pdf).
> It is worth noting that the sampling method used for generation is very critical to the quality of the output, which is a research topic worthy of further exploration. 

#### 3. How to finetune with my personal MIDI data?
Please see [issue/Training on custom MIDI corpus](https://github.com/YatingMusic/remi/issues/2)

## Acknowledgement
- The content of `modules.py` comes from the [kimiyoung/transformer-xl](https://github.com/kimiyoung/transformer-xl) repository.
- Thanks [@vibertthio](https://github.com/vibertthio) for the awesome online interactive demo.
