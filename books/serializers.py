from rest_framework import serializers

from books.models import Tag, Book


class NestedTagSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        return instance.name

    def to_internal_value(self, data):
        return data

    class Meta:
        model = Tag
        fields = []


class BookSerializer(serializers.ModelSerializer):
    tags = NestedTagSerializer(required=True, validators=[], many=True)

    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'tags']

    def validate(self, data):
        try:

            validation = super().validate(data)
            if len(data['tags']) != Tag.objects.all().filter(name__in=data['tags']).count():
                raise serializers.ValidationError({'tags': 'Some tags do not exist.'})
            return validation
        except serializers.ValidationError as err:
            raise err

    def create(self, validated_data):
        tags = validated_data.pop('tags')
        book = Book.objects.all().create(**validated_data)
        tags = Tag.objects.all().filter(name__in=tags)
        book.tags.add(*tags)
        print(tags)

        return book

    def update(self, instance, validated_data):
        tags = validated_data.pop('tags')
        book = Book.objects.all().create(**validated_data)
        tags = Tag.objects.all().filter(name__in=tags)
        book.tags.clear()
        book.tags.add(*tags)
        return super().update(instance, validated_data)

