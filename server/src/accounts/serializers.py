from rest_framework.serializers import (
    CharField, EmailField, HyperlinkedIdentityField, ModelSerializer, 
    ReadOnlyField, HyperlinkedRelatedField, BooleanField,
    HyperlinkedModelSerializer, SerializerMethodField, ValidationError)
from django.contrib.auth.models import User

from accounts.models import *
###########################################################
################## Create Serializers #####################
###########################################################
class UserCreateSerializer(ModelSerializer):
    email = EmailField(label='Email Address')
    email2 = EmailField(label='Confirm Email')
    first_name = CharField(label='First name', max_length=100)
    last_name = CharField(label='Last name', max_length=100)

    class Meta:
        model = User
        fields = [
            'username', 'first_name', 'last_name',
            'email', 'email2', 'password',
        ]
        extra_kwargs = {
            "password": {
                "write_only": True
            },
        }

    def validate(self, data):
        # email = data['email']
        # user_qs = User.objects.filter(email=email)
        # if user_qs.exists():
        #     raise ValidationError("This user has already registered.")
        return data

    def validate_email(self, value):
        data = self.get_initial()
        email1 = data.get("email2")
        email2 = value
        if email1 != email2:
            raise ValidationError("Emails must match.")

        user_qs = User.objects.filter(email=email2)
        if user_qs.exists():
            raise ValidationError("This user has already registered.")

        return value

    def validate_email2(self, value):
        data = self.get_initial()
        email1 = data.get("email")
        email2 = value
        if email1 != email2:
            raise ValidationError("Emails must match.")
        return value

    def create(self, validated_data):
        username = validated_data['username']
        email = validated_data['email']
        password = validated_data['password']
        first_name = validated_data['first_name']
        last_name = validated_data['last_name']

        user_obj = User(username=username, email=email, first_name=first_name, last_name=last_name, )
        user_obj.set_password(password)
        user_obj.save()
        subscriber_obj = Subscriber(user=user_obj)
        subscriber_obj.save()
        return validated_data


class TeamCreateSerializer(ModelSerializer):
    name = CharField(label='Team Name', max_length=200)
    
    class Meta:
        model = Team
        fields = ['name',]
        
       
    
    def create(self, validated_data):
      name = validated_data['name']

      new_team = Team(name=name,)
      new_team.save()
      return validated_data

class TeamTreeCreateSerializer(ModelSerializer):
    class Meta:
        model = TeamTree
        fields = ['parent', 'child',]
    
    def create(self, validated_data):
      parent = validated_data['parent']
      child = validated_data['child']

      new_team_relation = TeamTree(parent=parent, child=child)
      new_team_relation.save()
      
      return validated_data

class CompanyCreateSerializer(ModelSerializer):
    class Meta:
        model = Company
        fields = ['name']
    
    def create(self, validated_data):
      name = validated_data['name']

      new_company = Company(name=name)
      new_company.save()
      
      return validated_data

class TeamSubscriberCreateSerializer(ModelSerializer):
    manager = BooleanField(initial=False)
    class Meta:
        model = TeamSubscriber
        fields = ['team', 'subscriber', 'job_title', 'manager']
    
    def create(self, validated_data):
      team = validated_data['team']
      subscriber = validated_data['subscriber']
      job_title = validated_data['job_title']
      manager = validated_data['manager']

      new_TeamSubscriber = TeamSubscriber(
          team=team, subscriber=subscriber, job_title=job_title, manager=manager)
      new_TeamSubscriber.save()
      
      return validated_data

class CompanySubscriberCreateSerializer(ModelSerializer):
    class Meta:
        model = CompanySubscriber
        fields = ['company', 'subscriber',]
    
    def create(self, validated_data):
      company = validated_data['company']
      subscriber = validated_data['subscriber']

      new_CompanySubscriber = CompanySubscriber(company=company, subscriber=subscriber,)
      new_CompanySubscriber.save()
      
      return validated_data

class CompanyTeamCreateSerializer(ModelSerializer):
    class Meta:
        model = CompanyTeam
        fields = ['company', 'team',]
    
    def create(self, validated_data):
      company = validated_data['company']
      team = validated_data['team']

      new_CompanyTeam = CompanyTeam(company=company, team=team,)
      new_CompanyTeam.save()
      
      return validated_data
################################################################
################## View, Update & Delete #######################
################################################################
class UserSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email')

class SubscriberSerializer(HyperlinkedModelSerializer):
    # user = ReadOnlyField(source='user.username')
    user = UserSerializer()
    # user = HyperlinkedRelatedField(many=False, read_only=True, view_name='user-detail')
    class Meta:
        model = Subscriber
        fields = ('id', 'user', 'join_at', 'birthday', "timestamp", "updated", "active")

class TeamSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Team
        fields = ('id', "name", "timestamp", "updated", "active")

class CompanySerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Company
        fields = ('id', "name", "timestamp", "updated", "active")

class TeamTreeSerializer(HyperlinkedModelSerializer):
    parent = TeamSerializer()
    child = TeamSerializer()
   
    class Meta:
        model = TeamTree
        fields = ("id", "parent", "child", "timestamp", "updated", "active")

class TeamSubscriberSerializer(HyperlinkedModelSerializer):
    team = TeamSerializer()
    subscriber = SubscriberSerializer()
   
    class Meta:
        model = TeamSubscriber
        fields = ("id", "team", "subscriber", "job_title", "timestamp","manager", "updated", "active")

class CompanySubscriberSerializer(HyperlinkedModelSerializer):
    company = CompanySerializer()
    subscriber = SubscriberSerializer()
   
    class Meta:
        model = CompanySubscriber
        fields = ("id", "company", "subscriber", "timestamp", "updated", "active")
class CompanyTeamSerializer(HyperlinkedModelSerializer):
    company = CompanySerializer()
    team = TeamSerializer()
   
    class Meta:
        model = CompanyTeam
        fields = ("id", "company", "team", "timestamp", "updated", "active")



#
