# tensorflowOnM2

tested on mac mini m2 2023

```bash
# download a recent version of the script Miniconda3-latest-MacOSX-arm64.sh from https://developer.apple.com/metal/tensorflow-plugin/ (and better check the website) and copy it to this folder. now run
bash ./Miniconda3-latest-MacOSX-arm64.sh -b -p $HOME/miniconda

# actvate miniconda
source ~/miniconda/bin/activate

# install tensorflow-dependecies on apple channel
conda install -c apple tensorflow-deps

# install tensorflow for macos
python -m pip install tensorflow-macos

# and the package for GPU-Support
python -m pip install tensorflow-metal
 
# verify basic tensor-addtitions and driver usage
python tfdemofile.py

# ("Metal device set to: Apple M2" and a sum of "8" should be printed)

# verify if GPU used
python verifyTFwithGPU.py 
```

something similar to
```bash
782/782 [==============================] - 96s 108ms/step - loss: 4.7316 - accuracy: 0.0711  
Epoch 2/5
782/782 [==============================] - 81s 104ms/step - loss: 4.6754 - accuracy: 0.0631
Epoch 3/5
782/782 [==============================] - 81s 104ms/step - loss: 4.2070 - accuracy: 0.0868
Epoch 4/5
782/782 [==============================] - 81s 104ms/step - loss: 3.7748 - accuracy: 0.1332
Epoch 5/5
782/782 [==============================] - 80s 102ms/step - loss: 3.6772 - accuracy: 0.1575
```
should be printed


sources:
https://developer.apple.com/metal/tensorflow-plugin/
https://www.geeksforgeeks.org/install-tensorflow-on-macos/