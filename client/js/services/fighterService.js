
/**
 * FighterService is a service that provides methods to interact with the fighter data.
 * It can be used to fetch, create, update, and delete fighter information.
 */
export class FighterService {

  constructor(baseUrl) {
    this.baseUrl = baseUrl;
    this.token = localStorage.getItem('token');
  }

 
  async getAsync() {
    try {
      const response = await fetch(`${this.baseUrl}/api/fighters`, {
        method: 'GET',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${this.token}`
        }
      });

      if (!response.ok) {
        throw new Error('Failed to fetch fighters');
      }

      return await response.json();
    } catch (error) {
      console.error('Error fetching fighters:', error);
      return [];
    }
  }

  async getByIdAsync(fighterId) {
    try {
      const response = await fetch(`${this.baseUrl}/api/fighter/${fighterId}`, {
        method: 'GET',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${this.token}`
        }
      });
      if (!response.ok) {
        throw new Error('Failed to fetch fighter');
      }
      return await response.json();
    } catch (error) {
      console.error('Error fetching fighter:', error);
      return null;
    }
  }

  async createAsync(fighterData) {
    try {
      const response = await fetch(`${this.baseUrl}/api/fighter`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${this.token}`
        },
        body: JSON.stringify(fighterData)
      });

      if (!response.ok) {
        throw new Error('Failed to create fighter');
      }

      return await response.json();
    } catch (error) {
      console.error('Error creating fighter:', error);
      return null;
    }
  }

  async updateAsync(fighterId, fighterData) {
    try {
      const response = await fetch(`${this.baseUrl}/api/fighter/${fighterId}`, {
        method: 'PUT',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${this.token}`
        },
        body: JSON.stringify(fighterData)
      });

      if (!response.ok) {
        throw new Error('Failed to update fighter');
      }

      return await response.json();
    } catch (error) {
      console.error('Error updating fighter:', error);
      return null;
    }
  }

  async deleteAsync(fighterId) {
    try {
      const response = await fetch(`${this.baseUrl}/api/fighter/${fighterId}`, {
        method: 'DELETE',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${this.token}`
        }
      });

      if (!response.ok) {
        throw new Error('Failed to delete fighter');
      }

      return await response.json();
    } catch (error) {
      console.error('Error deleting fighter:', error);
      return null;
    }
  }


}