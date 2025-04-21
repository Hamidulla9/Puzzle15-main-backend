from django.db import models

class PlayerScore(models.Model):
    ip_address = models.GenericIPAddressField()
    moves = models.PositiveIntegerField()
    time_taken = models.PositiveIntegerField(help_text="Vaqt soniyalarda")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.ip_address} - {self.moves} moves - {self.time_taken}s"
