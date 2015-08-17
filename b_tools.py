# noinspection PyUnresolvedReferences
import bpy
from . import constants


# TODO: Should be in b_scene?
def object_on_layer(scene, obj, layer_numbers):
        """Checks if an object is on any of the layers represented by layer_numbers.

        Args:
            scene: The scene it will look in.
            obj: The object it will check.
            layer_numbers: A list consisiting of integers representing the layers that it will check
                if the object is on.

        Returns:
            True if the object is on any of the layers represented by layer_numbers, else False.
        """
        if obj in [e for e in scene.objects]:
            for n in layer_numbers:
                if obj.layers[n]:
                    return True

        return False


# TODO: Should be in b_scene?
def check_any_selected(scene, obj_types=constants.obj_types):
    """Checks the scene for if any object is selected.

    Args:
        scene: The scene to be checked.
        obj_types: An optional tuple consisting of strings representing the object type(s)
            that the object is allowed to be. If none specified, all types count.
    """
    # TODO: Optional tuple or list?
    for obj in scene.objects:
        if obj.type in obj_types and obj.select is True:
            return True

    return False


def layerlist_to_numberset(layer_list):
    """Converts a layer list to a number list.

    Converts a layer list consisting of booleans to a number list consisting of integers,
    representing the layers that are True in layer_list.

    Example:
        >>> print(layerlist_to_numberset([False, True, False, False, True]))
        [1, 4]

        This because layer 2 (index 1) and layer 3 (index 4) are both True.

    Args:
        layers: A list with booleans representing which layers are True and which are not.
            The first item represents the first layer and so on.

    Returns:
        A list consisting of integers representing the layers that are True in layer_list.
    """
    number_list = []

    for i in range(0, 20):
        if layer_list[i]:
            number_list.append(i)

    return set(number_list)


def manipulate_layerlists(mode, list1, list2):
    """Adds or subtracts two layer lists.

    If mode equals 'subtract' it subtracts list2 from list1.

    Example:
        >>> print(manipulate_layerlists('add', [False, True, True, False], [True, True, False, False]))
        [True, True, True, False]
        >>> print(manipulate_layerlists('subtract', [False, True, True, False], [True, True, False, False]))
        [False, False, True, False]

    Args:
        mode: A string, either 'add' to add the lists or 'subtract' to subtract them.
        list1: One of the layer lists you want to combine.
        list2: The other one of the layer lists you want to combine.

    Returns:
        The combined layer list.
    """
    layers = []

    if mode == 'add':
        for i in range(20):
            if list1[i] is True or list2[i] is True:
                layers.append(True)

            else:
                layers.append(False)

    elif mode == 'subtract':
        for i in range(20):
            if list1[i] is True and list2[i] is True:
                layers.append(False)

            else:
                layers.append(list1[i])

    return layers