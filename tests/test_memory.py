import unittest
from memory.trail_manager import TrailManager
from memory.memory_client import MemoryClient

class TestMemoryModule(unittest.TestCase):
    def test_trail_manager_append(self):
        trail = ['id1']
        parent_id = 'id2'
        updated_trail = TrailManager.append(trail, parent_id)
        self.assertEqual(updated_trail, ['id1', 'id2'])

    def test_memory_client_store_and_get(self):
        MemoryClient.clear_insights()
        insight = {'id': 'id1', 'content': 'Test insight'}
        MemoryClient.store_insight(insight)
        insights = MemoryClient.get_insights()
        self.assertIn(insight, insights)

    def test_memory_client_clear(self):
        MemoryClient.store_insight({'id': 'id2', 'content': 'Another insight'})
        MemoryClient.clear_insights()
        self.assertEqual(MemoryClient.get_insights(), [])
