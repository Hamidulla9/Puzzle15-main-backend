from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import PlayerScore
from .serializers import PlayerScoreSerializer

class SubmitScoreAPIView(APIView):
    def post(self, request):
        ip = self.get_client_ip(request)
        data = request.data.copy()
        data['ip_address'] = ip
        serializer = PlayerScoreSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip

class LeaderboardAPIView(APIView):
    def get(self, request):
        scores = PlayerScore.objects.all().order_by('time_taken')[:10]
        serializer = PlayerScoreSerializer(scores, many=True)
        return Response(serializer.data)
