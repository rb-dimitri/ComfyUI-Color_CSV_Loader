# Styles CSV Loader Extension for ComfyUI
Extension for [ComfyUI](https://github.com/comfyanonymous/ComfyUI) that loads color from a CSV file.
## Description
This extension allows users to load color strings to addd to your prompt from a CSV file (color.csv). 

## Installation
- Clone this repository into the `custom_nodes` folder of ComfyUI. Restart ComfyUI and the extension should be loaded.
- OR: Use the [ComfyUI-Manager](https://github.com/ltdrdata/ComfyUI-Manager) to install this extension.

**Important**: The `color.csv` file must be located in `ComfyUI/app/data` for seamless Baseten API integration.
## Nodes Description
Each color is represented as a dictionary with the keys being `color` and the values being a list containing `positive_prompt` and `negative_prompt`. The prompts are outputs of this Node.

## Author
- David Fischer
- minor changes by Dimitri E.
- GitHub: [theUpsider](https://github.com/theUpsider)
- Support the original author on [BuyMeACoffee](https://www.buymeacoffee.com/theupsider)
