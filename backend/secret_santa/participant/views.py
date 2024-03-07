from rest_framework import viewsets, mixins
from .models import Participant, Blacklist
from .serializers import ParticipantSerializer, BlacklistSerializer
from drf_spectacular.utils import extend_schema, OpenApiParameter, extend_schema_view


# Add the description for the participant endpoints
@extend_schema_view(
    list=extend_schema(description='Get the list of all the participants with their blacklist',
                        summary= 'Get the list of participants'),
    create=extend_schema(description='Create a new participant in the participant table',
                        summary='Add a participant'),
    retrieve=extend_schema(description='Find participant in the participant table',
                        summary='Retrieve a participant'),
    destroy=extend_schema(description='Delete a participant in the participant table',
                        summary='Remove a participant')
)
class ParticipantViewSet(mixins.CreateModelMixin,
                        mixins.RetrieveModelMixin,
                        mixins.DestroyModelMixin,
                        mixins.ListModelMixin,
                        viewsets.GenericViewSet):
    """ Class to handle our participant View Set """
    queryset = Participant.objects.all()
    serializer_class = ParticipantSerializer
    lookup_url_kwarg = "participant_id"


@extend_schema(
        parameters = [OpenApiParameter(name="participant_id", type=str, location=OpenApiParameter.PATH)]
)
# Add the description for the blacklist endpoints
@extend_schema_view(
    list=extend_schema(description='Get the list of blacklisted participants for a given person',
                        summary= 'Get the list of blacklisted participants'),
    create=extend_schema(description='Create a new entry to the participant blacklist',
                        summary='Add a participant to the blacklist'),
    destroy=extend_schema(description='Delete an entry to the participant blacklist',
                        summary='Remove a participant from the blacklist')
)
class BlacklistViewSet(mixins.CreateModelMixin,
                        mixins.DestroyModelMixin,
                        mixins.ListModelMixin,
                        viewsets.GenericViewSet):
    """ Class to handle our Blacklist View Set """
    serializer_class = BlacklistSerializer
    lookup_url_kwarg = "blacklist_id"
    
    def get_queryset(self):
        """ Get only the blacklist for the current participant """
        return Blacklist.objects.filter(owner_id=self.kwargs['participant_id'])
    
    def perform_create(self, serializer):
        """ Set automatically the participant_id value to the current participant """
        serializer.save(owner_id=self.kwargs["participant_id"])