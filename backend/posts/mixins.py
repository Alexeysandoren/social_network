from rest_framework.mixins import (CreateModelMixin, DestroyModelMixin,
                                   ListModelMixin)
from rest_framework.viewsets import GenericViewSet


class ListCreateDestroyView(
    ListModelMixin, CreateModelMixin, DestroyModelMixin, GenericViewSet
):
    pass
