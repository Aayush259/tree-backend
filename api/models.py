from django.db import models

class Node(models.Model):
    """
    A node is an entity that can have a parent and children. This means that a node can have multiple children but only one parent.
    A node can be a root node, which means it has no parent.
    """
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    data = models.CharField(max_length=500, blank=True, null=True)
    parent = models.ForeignKey('Node', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
