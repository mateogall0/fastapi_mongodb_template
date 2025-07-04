#!/usr/bin/env python3
from .emails import EmailSDK
from .files import FilesSDK
from .payments import PaymentsSDK

class BitaSDK(EmailSDK,
              FilesSDK,
              PaymentsSDK,):
    """
    All implementations of the sdk inherit from a core SDK implementation that
    handles the access and refresh tokens periodically using AsyncIO.

    Every feature is split into different classes that have specific endpoint
    prefixes inside their file definition to separate them. For instance, the
    email service endpoint is going to be handled in the `EmailSDK` class. If
    a new service is created, the way of implementing its calls to the SDK
    must inherit from `core` implementation and then this `BitaSDK` class must
    inherit from that new SDK.
    """