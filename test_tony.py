from recaudio import rec
import pytest
import _portaudio

def test_rec():
    """
    test recording
    """
    rec('test.wav')
    assert open(test.wav)  == ''