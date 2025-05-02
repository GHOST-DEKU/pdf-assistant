import typer
from typing import Optional, List
from phi.assistant import Assistant
from phi.storage.assistant.postgres import PgAssistantStorage
from phi.knowledge.pdf import PDFUrlKnowledge
from phi.vectordb.pgvector import Pgvector
import os
from dotenv import load_dotenv

load_dotenv("../env")




