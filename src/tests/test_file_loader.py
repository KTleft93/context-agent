import pytest
from unittest.mock import MagicMock, patch
from src.loaders.file_loader import load_and_split_pdf  # Replace 'your_module' with the actual module name

@patch("src.loaders.file_loader.RecursiveCharacterTextSplitter")
@patch("src.loaders.file_loader.PyPDFLoader")
def test_load_and_split_pdf(mock_pdf_loader, mock_text_splitter):
    # Arrange
    dummy_pdf_path = "sample.pdf"
    dummy_documents = ["doc1", "doc2"]
    dummy_chunks = ["chunk1", "chunk2", "chunk3"]

    # Mock the PDF loader behavior
    mock_loader_instance = MagicMock()
    mock_loader_instance.load.return_value = dummy_documents
    mock_pdf_loader.return_value = mock_loader_instance

    # Mock the text splitter behavior
    mock_splitter_instance = MagicMock()
    mock_splitter_instance.split_documents.return_value = dummy_chunks
    mock_text_splitter.return_value = mock_splitter_instance

    # Act
    result = load_and_split_pdf(dummy_pdf_path, chunk_size=500, chunk_overlap=100)

    # Assert
    mock_pdf_loader.assert_called_once_with(dummy_pdf_path)
    mock_loader_instance.load.assert_called_once()
    mock_text_splitter.assert_called_once_with(chunk_size=500, chunk_overlap=100)
    mock_splitter_instance.split_documents.assert_called_once_with(dummy_documents)
    assert result == dummy_chunks
