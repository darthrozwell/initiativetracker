class AddEncFailedError(Exception):
    pass

class AddCombFailedError(Exception):
    pass

class UpdateEncFailedError(Exception):
    pass

class UpdateCombFailedError(Exception):
    pass

class DeleteEncFailedError(Exception):
    pass

class DeleteEncNotFoundError(Exception):
    pass

class DeleteCombFailedError(Exception):
    pass

class DeleteCombNotFoundError(Exception):
    pass

class CombatantHasNoTypeError(Exception):
    pass
