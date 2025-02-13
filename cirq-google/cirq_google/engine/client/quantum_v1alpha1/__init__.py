# Copyright 2020 The Cirq Developers
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import absolute_import
import sys
import warnings

from cirq_google.engine.client.quantum_v1alpha1 import types
from cirq_google.engine.client.quantum_v1alpha1.gapic import enums
from cirq_google.engine.client.quantum_v1alpha1.gapic import quantum_engine_service_client

if sys.version_info[:2] == (2, 7):
    message = (
        'A future version of this library will drop support for Python 2.7.'
        'More details about Python 2 support for Google Cloud Client Libraries'
        'can be found at https://cloud.google.com/python/docs/python2-sunset/'
    )
    warnings.warn(message, DeprecationWarning)


class QuantumEngineServiceClient(quantum_engine_service_client.QuantumEngineServiceClient):
    __doc__ = quantum_engine_service_client.QuantumEngineServiceClient.__doc__
    enums = enums


__all__ = (
    'enums',
    'types',
    'QuantumEngineServiceClient',
)
