import pytest
from unittest.mock import patch, MagicMock
from project import (
    get_user_input, 
    search_track, 
    process_results, 
    create_playlist, 
    view_playlist, 
    delete_playlist, 
    get_history, 
    clear_history, 
    write_history, 
    pluck
)
from lib.track import Track
from lib.history import History
from lib.playlist import Playlist
from lib.spotify import Spotify

def test_get_user_input():
    with patch('builtins.input', side_effect=['1']):
        assert get_user_input() == 1

def test_create_playlist():
    with patch('builtins.input', side_effect=['Test Playlist', 'no']), \
         patch('project.search_track') as mock_search, \
         patch('project.process_results') as mock_process, \
         patch('project.Playlist.create') as mock_create:
        
        mock_search.return_value = [{'name': 'Test Song', 'uri': 'test:uri', 'artists': [{'name': 'Test Artist'}]}]
        mock_process.return_value = Track('Test Song', 'test:uri', ['Test Artist'])
        
        create_playlist()
        mock_create.assert_called_once()

def test_view_playlist():
    with patch('builtins.input', side_effect=['1']), \
         patch('project.Playlist.list') as mock_list, \
         patch('project.Playlist.view') as mock_view:
        
        mock_list.return_value = ['Test Playlist']
        mock_view.return_value = [{'title': 'Test Song', 'artists': 'Test Artist', 'tempo': 120, 'time_signature': 4}]
        
        view_playlist()
        mock_view.assert_called_once()

def test_delete_playlist():
    with patch('builtins.input', side_effect=['1']), \
         patch('project.Playlist.list') as mock_list, \
         patch('project.Playlist.delete') as mock_delete:
        
        mock_list.return_value = ['Test Playlist']
        
        delete_playlist()
        mock_delete.assert_called_once()

def test_clear_history():
    with patch('project.History.clear') as mock_clear, \
         patch('sys.exit') as mock_exit:
        
        clear_history()
        
        mock_clear.assert_called_once()
        mock_exit.assert_called_once_with("Successfully cleared history")

def test_write_history():
    mock_track = Track('Test Song', 'test:uri', ['Test Artist'], 120, 4)
    with patch.object(History, 'write', return_value=None) as mock_write:
        write_history(mock_track)
        mock_write.assert_called_once_with(mock_track)

def test_pluck():
    list_of_dicts = [{'name': 'Test1'}, {'name': 'Test2'}, {'name': 'Test3'}]
    result = pluck(list_of_dicts, 'name')
    assert result == ['Test1', 'Test2', 'Test3']
