# HEALIX
A Dataset and Resources for Identifying Patient Health Literacy Information from Clinical Notes

# Requirements
Python 3.x

# Loading the Dataset
To access HEALIX it requires credentialed access via Physionet
Once you have downloaded `healix.json`, you can load it as follows:

    python loading_HEALIX.py

Or within your own script:

    from loading_HEALIX import load_healix
    data = load_healix("HEALIX.json")
