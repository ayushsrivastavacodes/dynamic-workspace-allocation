# Dynamic Workspace Allocation System

An AI-driven solution for dynamic workspace allocation using decision trees, priority-based search, and online learning.

## 🚀 Features

- **Decision Trees for Initial Allocation**: Quick workspace predictions based on historical data
- **Priority-Based Search**: Real-time optimization with Best-First Search
- **Online Learning**: Continuous improvement through rolling window updates
- **Hierarchical Clustering**: Efficient grouping of similar workspace requests
- **Predictive Modeling**: Peak demand forecasting
- **Fairness Constraints**: Ensures equitable workspace distribution
- **User Feedback Integration**: Real-time adjustments based on satisfaction

## 🏢 Workspace Types Supported

- Private Offices
- Managerial Cabins
- Fixed Workstations
- Hot Desks
- Meeting Rooms
- Conference Halls
- Collaboration Spaces
- Breakout Areas

## 📋 Prerequisites

- Python 3.9+
- pip

## 🛠️ Installation

1. Clone the repository:
```bash
git clone https://github.com/ayushsrivastavacodes/dynamic-workspace-allocation.git
cd dynamic-workspace-allocation
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## 🏃‍♂️ Running the Application

1. Start the API server:
```bash
uvicorn app.main:app --reload
```

2. Access the API documentation:
```
http://localhost:8000/docs
```

## 🧪 Running Tests

```bash
pytest
```

## 📚 Project Structure

```
dynamic-workspace-allocation/
├── app/
│   ├── api/              # API endpoints
│   ├── core/             # Core business logic
│   ├── models/           # Data models
│   └── utils/            # Utility functions
├── tests/                # Test suite
├── requirements.txt      # Project dependencies
└── README.md            # Project documentation
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.