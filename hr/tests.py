from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import CustomUser, Employees, Tasks

class CustomUserModelTest(TestCase):
    def test_user_creation(self):
        User = get_user_model()
        user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )
        self.assertIsInstance(user, CustomUser)
        self.assertEqual(user.username, 'testuser')
        self.assertEqual(user.user_type, 1)

class EmployeesModelTest(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(
            username='testuser',
            password='testpassword'
        )
        self.employee = Employees.objects.create(
            user=self.user,
            name='John Doe',
            email='johndoe@gmail.com',
            contact=1234567890,
            gender='Male',
            department='IT',
            position='Developer',
            dor='2023-01-01'
        )

    def test_employee_creation(self):
        self.assertEqual(self.employee.name, 'John Doe')
        self.assertEqual(self.employee.email, 'johndoe@gmail.com')
        self.assertEqual(self.employee.contact, 1234567890)
        self.assertEqual(self.employee.gender, 'Male')
        self.assertEqual(self.employee.department, 'IT')
        self.assertEqual(self.employee.position, 'Developer')
        self.assertEqual(str(self.employee.dor), '2023-01-01')

    def test_employee_str_representation(self):
        self.assertEqual(str(self.employee), 'John Doe')

class TasksModelTest(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(
            username='testuser',
            password='testpassword'
        )
        self.task = Tasks.objects.create(
            employee=self.user,
            title='Task 1',
            description='Task 1 description',
            status='To DO',
            start_date='2023-01-01',
            due_date='2023-01-10'
        )

    def test_task_creation(self):
        self.assertEqual(self.task.title, 'Task 1')
        self.assertEqual(self.task.description, 'Task 1 description')
        self.assertEqual(self.task.status, 'To DO')
        self.assertEqual(str(self.task.start_date), '2023-01-01')
        self.assertEqual(str(self.task.due_date), '2023-01-10')

    def test_task_str_representation(self):
        self.assertEqual(str(self.task), 'Task 1')
