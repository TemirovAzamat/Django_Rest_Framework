from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response


class MyGenericRetrieveUpdateDestroyAPIView(APIView):
    queryset = None
    serializer_class = None

    def get_object(self, pk):
        return get_object_or_404(self.queryset.all(), pk=pk)

    def get(self, request, pk, *args, **kwargs):
        serializer = self.serializer_class(instance=self.get_object(pk))
        return Response(serializer.data, status=201)

    def put(self, request, pk, *args, **kwargs):
        serializer = self.serializer_class(instance=self.get_object(pk), data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response(serializer.errors, status=400)

    def delete(self, request, pk, *args, **kwargs):
        self.get_object(pk).delete()
        return Response(status=204)
