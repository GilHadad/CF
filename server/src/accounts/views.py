from django.contrib.auth        import get_user_model
from rest_framework.generics    import CreateAPIView, ListCreateAPIView
from django.contrib.auth.models import User

from rest_framework             import generics
from rest_framework.response    import Response
from rest_framework.reverse     import reverse
from rest_framework             import permissions

from accounts.serializers       import *
from accounts.models            import *

User = get_user_model()


def get_subscriber_company(user):
    subscriber = Subscriber.objects.get(user=user)
    companies = CompanySubscriber.objects.all()
    for company in companies:
        if company.subscriber == subscriber:
            return company.company



def get_subscriber_teams_qs(self):
    user = self.request.user
    teams = TeamSubscriber.objects.filter(subscriber=subscriber)

    subscriber_teams = []
    for team in teams:
        subscriber_teams.append(team.id)

    return Team.objects.filter(pk__in=subscriber_teams)


def get_company_teams_qs(self):
    user = self.request.user
    company = get_subscriber_company(user)
    company_teams = CompanyTeam.objects.filter(company=company)

    teams = []
    for team in company_teams:
        teams.append(team.id)

    return Team.objects.filter(pk__in=teams)
def get_company_subscribers_qs(self):
    user = self.request.user
    company = get_subscriber_company(user)
    company_subscribers = CompanySubscriber.objects.filter(company=company)

    subscribers = []
    for subscriber in company_subscribers:
        subscribers.append(subscriber.subscriber.id)


    return Subscriber.objects.filter(id__in=subscribers)

def get_company_users_qs(self):
    user = self.request.user
    company = get_subscriber_company(user)
    company_subscribers = CompanySubscriber.objects.filter(company=company)

    users = []
    for subscriber in company_subscribers:
        users.append(subscriber.subscriber.user.id)


    return User.objects.filter(id__in=users)

####################### USERS ##################################
class UserDetailAPIView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]
    name = 'user-details'

class UserListAPIView(generics.ListAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]
    name = 'user-list'

    def get_queryset(self):
        return get_company_users_qs(self)

####################### SUBSCRIBERS ############################
class SubscriberCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer
    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny]
    name = 'register'

class SubscriberDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Subscriber.objects.all()
    serializer_class = SubscriberSerializer
    permission_classes = [permissions.AllowAny]
    name = 'subscriber-details'

class SubscriberListAPIView(generics.ListAPIView):
    serializer_class = SubscriberSerializer
    permission_classes = [permissions.AllowAny]
    name = 'subscriber-list'

    def get_queryset(self):
        return get_company_subscribers_qs(self)

####################### TEAM ###################################
class TeamCreateAPIView(CreateAPIView):
    serializer_class = TeamCreateSerializer
    queryset = Team.objects.all()
    permission_classes = [permissions.AllowAny]
    name = 'team-create' 

class TeamDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    permission_classes = [permissions.AllowAny]
    name = 'team-detail'

class TeamListAPIView(generics.ListAPIView):
    # queryset = Team.objects.all()
    serializer_class = TeamSerializer
    permission_classes = [permissions.IsAuthenticated]
    name = 'team-list'
    def get_queryset(self):
        return get_company_teams_qs(self)


####################### COMPANY ################################
class CompanyCreateAPIView(CreateAPIView):
    serializer_class = CompanyCreateSerializer
    queryset = Company.objects.all()
    permission_classes = [permissions.AllowAny]
    name = 'company-create'

class CompanyDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [permissions.AllowAny]
    name = 'company-detail'

class CompanyListAPIView(generics.ListAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [permissions.AllowAny]
    name = 'company-list'
####################### RELATIONS CREATE #######################
class TeamTreeCreateAPIView(CreateAPIView):
    serializer_class = TeamTreeCreateSerializer
    queryset = TeamTree.objects.all()
    permission_classes = [permissions.AllowAny]
    name = 'creat-team-relation'

class TeamSubscriberCreateAPIView(CreateAPIView):
    queryset = TeamSubscriber.objects.all()
    serializer_class = TeamSubscriberCreateSerializer
    permission_classes = [permissions.AllowAny]
    name = 'creat-TeamSubscriber-relation'

class CompanySubscriberCreateAPIView(CreateAPIView):
    serializer_class = CompanySubscriberCreateSerializer
    permission_classes = [permissions.AllowAny]
    name = 'creat-CompanySubscriber-relation'
    def get_queryset(self):
        return get_company_subscribers_qs(self)

class CompanyTeamCreateAPIView(CreateAPIView):
    serializer_class = CompanyTeamCreateSerializer
    permission_classes = [permissions.AllowAny]
    name = 'creat-CompanyTeam-relation'
    def get_queryset(self):
        return get_company_teams_qs(self)

####################### RELATIONS VIEWS ########################
class TeamTreeAPIView(generics.ListAPIView):
    queryset = TeamTree.objects.all()
    serializer_class = TeamTreeSerializer
    permission_classes = [permissions.AllowAny]
    name = 'team-relations'


class TeamSubscriberAPIView(generics.ListAPIView):
    queryset = TeamSubscriber.objects.all()
    serializer_class = TeamSubscriberSerializer
    permission_classes = [permissions.AllowAny]
    name = 'TeamSubscriber-relations'





class CompanySubscriberAPIView(generics.ListAPIView):
    serializer_class = CompanySubscriberSerializer
    permission_classes = [permissions.AllowAny]
    name = 'CompanySubscriber-relations'

    def get_queryset(self):
        return get_company_subscribers_qs(self)



class CompanyTeamAPIView(generics.ListAPIView):
    serializer_class = CompanyTeamSerializer
    permission_classes = [permissions.AllowAny]
    name = 'CompanyTeam-relations'
    def get_queryset(self):
        return get_company_teams_qs(self)

# need to add "my team subscriber" ????
