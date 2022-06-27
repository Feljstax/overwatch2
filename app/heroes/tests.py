from django.test import TestCase
from django.urls import reverse
import pytest
from heroes.models import Hero

# Create your tests here.

#Unit test
def test_homepage_access():
    url = reverse('home')
    assert url == "/"

#Integration testing
@pytest.mark.django_db
def test_create_hero():
    hero = Hero.objects.create(
        name='TestHero',
        hp='200',
        pick_ranking='1`',
        role_type='1'

    )
    assert hero.name == "Pytest"

@pytest.fixture
def new_hero(db):
    hero = Hero.objects.create(
        name='TestHero',
        hp='200',
        pick_ranking='1`',
        role_type='1'
    )
    return hero

def test_search_heroes(new_hero):
    assert Hero.objects.filter(name='TestHero').exists()

def test_update_hero(new_hero):
    new_hero.name = 'UpdatedHero'
    new_hero.save()
    assert Hero.objects.filter(name='UpdatedHero').exists()

@pytest.fixture
def another_hero(db):
    hero = Hero.objects.create(
        name='Hero2',
        hp='200',
        pick_ranking='4`',
        role_type='1'
    )
    return hero

def test_compare_heroes(new_hero, another_hero):
    assert new_hero.pk != another_hero.pk