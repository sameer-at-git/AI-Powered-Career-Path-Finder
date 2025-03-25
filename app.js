document.getElementById('careerForm').addEventListener('submit', async function(e) {
    e.preventDefault();
    
    const name = document.getElementById('name').value;
    const skills = document.getElementById('skills').value;
    const experience = document.getElementById('experience').value;
    
    const requestData = { name, skills, experience };
    
    try {
      const response = await fetch('http://localhost:8000/api/career-recommendation', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(requestData)
      });
      
      const result = await response.json();
      document.getElementById('result').innerHTML = `<strong>Recommendation:</strong> ${result.recommendation}`;
    } catch (error) {
      console.error('Error:', error);
      document.getElementById('result').textContent = 'Error fetching recommendation.';
    }
  });
  