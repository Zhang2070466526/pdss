from utils.genericMethods import ViewBasicTemplate
from .methods import BasicMobilize, MobilizeInfoFileClass


class basicDepartInfo(ViewBasicTemplate):
    def __init__(self):
        super().__init__(BasicMobilize)


class fileMobilizeInfo(ViewBasicTemplate):
    def __init__(self):
        super().__init__(MobilizeInfoFileClass)


def data_sync(request):
    bm = BasicMobilize(request)
    bm.add_meth()
    res = bm.method_center('data_sync')
    return res




