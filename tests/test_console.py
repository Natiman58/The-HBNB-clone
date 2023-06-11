#!/usr/bin/python3
"""
    A test module for all the console methods
"""
import unittest
from unittest import TestCase, mock
from console import HBNBCommand
from io import StringIO
from models.base_model import BaseModel
from uuid import uuid4
from models import storage


class TestConsole(TestCase):
    """
        Test Console methods
    """

    @classmethod
    def setUp(self):
        """ Set up the console for running tests """
        self.console = HBNBCommand()

    @classmethod
    def tearDown(self):
        """ Clean up the console after running tests """
        pass

    def test_EOF(self):
        """ Test EOF file command returns True """
        with mock.patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("EOF")
            self.assertEqual(f.getvalue(), "")

    def test_quit(self):
        """ Test the quit command returns True """
        with mock.patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("quit")
            self.assertEqual(f.getvalue(), "")

    def test_create(self):
        """ Test the create command returns the obj id """
        # when class name is missing
        with mock.patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create"))
            self.assertEqual(f.getvalue(), "** class name missing **\n")

        # when wrong class name is put in
        with mock.patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create MyModel"))
            self.assertEqual(f.getvalue(), "** class doesn't exist **\n")

        # when the parameters are added and class name is wrong
        with mock.patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create MyModel name='California' city_id='1234' location='USA'"))
            self.assertEqual(f.getvalue(), "** class doesn't exist **\n")

        # to theck it's output is uuid format
        with mock.patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            output = f.getvalue().strip()
            self.assertRegex(output, r'^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$')

    def test_show(self):
        """Test the show method"""
        # When class name is missing
        with mock.patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("show"))
            self.assertEqual(f.getvalue(), "** class name missing ** \n")

        # When class does not exist
        with mock.patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("show MyModel"))
            self.assertEqual(f.getvalue(), "** class doesn't exist **\n")

        # when the id is missing
        with mock.patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("show BaseModel"))
            self.assertEqual(f.getvalue(), "** instance id missing **\n")

        # when the instance of the class doesn't exist for the id
        with mock.patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("show BaseModel 121212"))
            self.assertEqual(f.getvalue(), "** no instance found **\n")

        # create a new instance and ...
        with mock.patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            obj_id = f.getvalue().strip()

        # then test correct output; should be the object
        with mock.patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd(f"show BaseModel {obj_id}"))
            expected_output = str(storage.all()[f"BaseModel.{obj_id}"]).strip()
            self.assertEqual(f.getvalue().strip(), expected_output)

    def test_destroy(self):
        """Test the destroy method"""
        # when class name  is missing
        with mock.patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("destroy"))
            self.assertEqual(f.getvalue().strip(), "** class name missing **")

        # when the class doesn't exist
        with mock.patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("destroy MyModel"))
            self.assertEqual(f.getvalue().strip(), "** class doesn't exist **")

        # when the id is missing
        with mock.patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("destroy BaseModel"))
            self.assertEqual(f.getvalue().strip(), "** instance id missing **")

        # when the instance of the class name doesn't exist for the id
        with mock.patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("destroy BaseModel 121212"))
            self.assertEqual(f.getvalue().strip(), "** no instance found **")

        # creeate new instance and get the id
        with mock.patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            obj_id = f.getvalue().strip()

        # then check the correct output
        with mock.patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd(f"destroy BaseModel {obj_id}"))
            expected_output = ""
            self.assertEqual(f.getvalue().strip(), expected_output)

    def test_all(self):
        """Test the all methods"""

        # when class name doesn't exist
        with mock.patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("all MyModel"))
            self.assertEqual(f.getvalue().strip(), "** class doesn't exist **")

        # check the correct output
        #with mock.patch('sys.stdout', new=StringIO()) as f:
        #    self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
        #    obj_id = f.getvalue().strip()
        #with mock.patch('sys.stdout', new=StringIO()) as f:
        #    self.assertFalse(HBNBCommand().onecmd("all BaseModel"))
        #    obj_repr = str(storage.all()["BaseModel." + obj_id])
        #    attrs = obj_repr.split(",")[1][:-1].strip()
        #    expected_output = f'[BaseModel] ({obj_id} {attrs})'
        #    self.assertEqual(f.getvalue().strip(), [expected_output])

    def test_update(self):
        """Test the update method"""

        # when class name is missing
        with mock.patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("update"))
            self.assertEqual(f.getvalue().strip(), "** class name missing **")

        # when class name doesn't exist
        with mock.patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("update MyModel"))
            self.assertEqual(f.getvalue().strip(), "** class doesn't exist **")

        # when id is missing
        with mock.patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("update BaseModel"))
            self.assertEqual(f.getvalue().strip(), "** instance id missing **")

        # if the instance of the class name doesn't exist for the if
        with mock.patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("update BaseModel 121212"))
            self.assertEqual(f.getvalue().strip(), "** no instance found **")

        # get the obj id first
        with mock.patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            obj_id = f.getvalue().strip()
        # then test if the attribute name is missing
        with mock.patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd(f"update BaseModel {obj_id}"))
            self.assertEqual(f.getvalue().strip(), "** attribute name missing **")
        # then test if the value is missing
        with mock.patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd(f"update BaseModel {obj_id} first_name"))
            self.assertEqual(f.getvalue().strip(), "** value missing **")
        # then test if all arguments are being used
        with mock.patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd('update BaseModel 1234-1234-1234 email "aibnb@mail.com" first_name "Betty" = $ update BaseModel 1234-1234-1234 email "aibnb@mail.com")'))
            self.assertEqual(f.getvalue().strip(), "** All other arguments shouldn't be used once **")



if __name__ == '__main__':
    unittest.main()
