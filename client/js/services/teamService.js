export class TeamService {
  constructor(baseUrl) {
    this.baseUrl = baseUrl;
    this.token = localStorage.getItem('token');
  }

  async getAsync() {
    try {
      const response = await fetch(`${this.baseUrl}/api/teams`, {
        method: 'GET',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${this.token}`
        }
      });

      if (!response.ok) {
        throw new Error('Failed to fetch teams');
      }

      return await response.json();
    } catch (error) {
      console.error('Error fetching teams:', error);
      return [];
    }
  }

  async createAsync(teamData) {
    try {
      const response = await fetch(`${this.baseUrl}/api/team`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${this.token}`
        },
        body: JSON.stringify(teamData)
      });

      if (!response.ok) {
        throw new Error('Failed to create team');
      }

      return await response.json();
    } catch (error) {
      console.error('Error creating team:', error);
      return null;
    }
  }

  async updateAsync(teamId, teamData) {
    try {
      const response = await fetch(`${this.baseUrl}/api/team/${teamId}`, {
        method: 'PUT',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${this.token}`
        },
        body: JSON.stringify(teamData)
      });

      if (!response.ok) {
        throw new Error('Failed to update team');
      }

      return await response.json();
    } catch (error) {
      console.error('Error updating team:', error);
      return null;
    }
  }

  async deleteAsync(teamId) {
    try {
      const response = await fetch(`${this.baseUrl}/api/team/${teamId}`, {
        method: 'DELETE',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${this.token}`
        }
      });

      if (!response.ok) {
        throw new Error('Failed to delete team');
      }

      return await response.json();
    } catch (error) {
      console.error('Error deleting team:', error);
      return null;
    }
  }
}