class JobRole:
    def __init__ (self,domain, position, experience, tech_needed):
        self.domain = domain
        self.position= position
        self.experience= experience
        if isinstance(tech_needed, str):
            self.tech_needed = [tech.strip() for tech in tech_needed.split(",") if tech.strip()]
        elif isinstance(tech_needed, list):
            self.tech_needed = tech_needed
        else:
            raise TypeError("tech_needed must be a string or a list")

    def __str__(self):
        return f"{self.domain} | {self.position} | {self.experience} | {', '.join(self.tech_needed)}"
    
    def to_dict(self):
        return { "domain": self.domain,
                "position": self.position,
                "experience": self.experience,
                "tech_needed": self.tech_needed
                  }
    
    @staticmethod
    def from_dict(data):
        return JobRole(
        domain= data["domain"],
        position= data["position"],
        experience= data["experience"],
        tech_needed= data["tech_needed"]
        )
    def summary(self):
        return {
        "Domain": self.domain,
        "Position": self.position,
        "Experience": self.experience,
        "Tech Needed": self.tech_needed
    }

        
        
        