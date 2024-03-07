from rest_framework import viewsets, mixins
from .models import Draw, DrawResult
from .serializers import DrawSerializer, DrawResultSerializer, DrawPostSerializer
from drf_spectacular.utils import extend_schema, OpenApiParameter, extend_schema_view


# Add the description for the Draw endpoints
@extend_schema_view(
    list=extend_schema(description='Get the list of the draws sorted by descending creation_time',
                        summary= 'Get the draw sorted by descending creation_time'),
    create=extend_schema(description='Create a new draw in the Draw table',
                        summary='Add a draw'),
    retrieve=extend_schema(description='Find draw in the draw table',
                        summary='Retrieve a draw'),
    destroy=extend_schema(description='Delete a draw in the draw table',
                        summary='Remove a draw')
)
class DrawViewSet(mixins.CreateModelMixin,
                        mixins.RetrieveModelMixin,
                        mixins.DestroyModelMixin,
                        mixins.ListModelMixin,
                        viewsets.GenericViewSet):
    """ Class to handle our draw View Set """
    # Return the draws sorted by descending creation_time
    queryset = Draw.objects.all().order_by('-creation_time')
    lookup_url_kwarg = "draw_id"

    # Use of a different serializer for the create method
    def get_serializer_class(self):
        if self.action == 'create':
            return DrawPostSerializer
        else: 
            return DrawSerializer


@extend_schema(
        parameters = [OpenApiParameter(name="draw_id", type=str, location=OpenApiParameter.PATH)]
)
# Add the description for the DrawResult endpoints
@extend_schema_view(
    list=extend_schema(description='Get the list of draw results for a given draw',
                        summary= 'Get the list of draw results'),
    create=extend_schema(description='Create a new draw result',
                        summary='Add a draw result')
)
class DrawResultViewSet(mixins.CreateModelMixin,
                        mixins.ListModelMixin,
                        viewsets.GenericViewSet):
    """ Class to handle our DrawResult View Set """
    serializer_class = DrawResultSerializer

    def get_queryset(self):
        """ Get only the DrawResult for the current draw """
        return DrawResult.objects.filter(draw_id=self.kwargs['draw_id'])

    def perform_create(self, serializer):
        """ Set automatically the draw_id value to the current DrawResult """
        serializer.save(draw_id=self.kwargs["draw_id"])