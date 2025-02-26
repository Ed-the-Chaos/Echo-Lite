from akr_module import AdaptiveKnowledgeRefinement

class EchoLite:
    def __init__(self):
        self.akr = AdaptiveKnowledgeRefinement()

    def process_input(self, key, information):
        """Processes new information and refines knowledge dynamically."""
        self.akr.refine_knowledge(key, information)
        return f"Processed: {key}"

    def get_knowledge(self):
        """Returns the current knowledge base."""
        return self.akr.show_knowledge()

    def get_refinement_log(self):
        """Returns the refinement log."""
        return self.akr.show_refinement_log()

# Example Usage (To be removed when integrated into full system)
if __name__ == "__main__":
    echo = EchoLite()
    echo.process_input("AI", "Artificial Intelligence is advancing.")
    echo.process_input("AI", "AI is evolving through self-learning.")
    print("Knowledge Base:", echo.get_knowledge())
    print("Refinement Log:", echo.get_refinement_log())
