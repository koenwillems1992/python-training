"""
Demo 5
"""

from typing import Dict, List, Union

y: List[Union[int, float]] = [1, 2.0]
z: Dict[Union[float], Dict[str, str]] = {1: {"name": "Jane"}, 2: {"name": "John"}}
print(z)
