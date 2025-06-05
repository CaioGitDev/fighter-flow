DevExpress.config({
  editorStylingMode: "underlined" // or 'outlined' | 'underlined'
});

import { FighterService } from "../../js/services/fighterService.js";
import { TeamService } from "../../js/services/teamService.js";

const baseUrl = 'http://127.0.0.1:5000';


function createCustomStore(service) {
  return new DevExpress.data.CustomStore({
    key: 'id',
    load: async () => {
      const { data } = await service.getAsync();
      return data;
    },
    insert: async (values) => {
      const result = await service.createAsync(values);
      return result;
    },
    update: async (key, values) => {
      const result = await service.updateAsync(key, values);
      return result;
    },
    remove: async (key) => {
      const result = await service.deleteAsync(key);
      return result;
    }
  });
}

async function buildAthleteManagementDataGrid(container) {
  
  const teamService = new TeamService(baseUrl);
  let teams = [];
  try {
    const { data } = await teamService.getAsync();
    teams = data.map(team => ({ id: team.id, name: team.name }));
  } catch (error) {
    console.error('Error fetching teams:', error);
    return;
  }

  const dataGrid = document.createElement('div');
  dataGrid.id = 'athlete-management-grid';
  dataGrid.className = 'dx-datagrid';

  container.appendChild(dataGrid);

  const fighterService = new FighterService(baseUrl);
  try {
    $(dataGrid).dxDataGrid({
      dataSource: createCustomStore(fighterService),
      keyExpr: 'id',
      showBorders: true,
      height: 500,

      editing: {
        mode: "popup",
        allowUpdating: true,
        allowAdding: true,
        allowDeleting: true,
        useIcons: true,
        popup: {
          title: "Atleta",
          showTitle: true,
          width: 600,
          height: 'auto'
        },
        form: {
          items: [
            { dataField: "first_name", validationRules: [{ type: "required" }] },
            { dataField: "last_name", validationRules: [{ type: "required" }] },
            { dataField: "nickname" },
            {
              dataField: "weight",
              editorType: "dxNumberBox",
              validationRules: [
                { type: "required" },
                { type: "range", min: 0, max: 200, message: "Peso deve estar entre 0 e 200 kg" }
              ]
            },
            {
              dataField: "team_id",
              editorType: "dxSelectBox",
              editorOptions: {
                dataSource: teams, // Certifica-te que tens este array com { id, name }
                valueExpr: "id",
                displayExpr: "name"
              },
              validationRules: [{ type: "required" }]
            },
            {
              dataField: "wins",
              editorType: "dxNumberBox",
              validationRules: [{ type: "required" }, { type: "range", min: 0 }]
            },
            {
              dataField: "losses",
              editorType: "dxNumberBox",
              validationRules: [{ type: "required" }, { type: "range", min: 0 }]
            },
            {
              dataField: "draws",
              editorType: "dxNumberBox",
              validationRules: [{ type: "required" }, { type: "range", min: 0 }]
            },
            {
              dataField: "active",
              editorType: "dxCheckBox"
            }
          ]
        }
      },
      columnAutoWidth: true,
      toolbar: {
        items: [
          {
            name: 'addRowButton',
            showText: 'always',
            location: 'after',
            widget: 'dxButton',
            options: {
              icon: 'add',
              text: 'Adicionar Atleta',
              onClick: () => {
                $(dataGrid).dxDataGrid('instance').addRow();
              }
            }
          },
          {
            name: 'refreshButton',
            showText: 'always',
            location: 'after',
            widget: 'dxButton',
            options: {
              icon: 'refresh',
              text: 'Refresh',
              onClick() {
                $(dataGrid).dxDataGrid('instance').refresh();
              }
            }
          }
        ]
      },
      columns: [
        { dataField: 'first_name', caption: 'First Name' },
        { dataField: 'last_name', caption: 'Last Name' },
        { dataField: 'nickname', caption: 'Nickname' },
        {
          dataField: 'weight',
          caption: 'Weight (kg)',
          dataType: 'number'
        },
        {
          dataField: 'team_id',
          caption: 'Team',
          lookup: {
            dataSource: teams, // [{ id: 1, name: 'CT - Team' }, ...]
            valueExpr: 'id',
            displayExpr: 'name'
          }
        },
        {
          dataField: 'wins',
          caption: 'Wins',
          dataType: 'number'
        },
        {
          dataField: 'losses',
          caption: 'Losses',
          dataType: 'number'
        },
        {
          dataField: 'draws',
          caption: 'Draws',
          dataType: 'number'
        },
        {
          dataField: 'active',
          caption: 'Active',
          dataType: 'boolean'
        },
        {
          dataField: 'created_at',
          caption: 'Created',
          dataType: 'date',
          format: 'shortDateShortTime',
          allowEditing: false,
          visible: false
        },
        {
          dataField: 'updated_at',
          caption: 'Updated',
          dataType: 'date',
          format: 'shortDateShortTime',
          allowEditing: false,
          visible: false
        }
      ],

      paging: {
        pageSize: 10
      },
      pager: {
        showPageSizeSelector: true,
        allowedPageSizes: [5, 10, 20],
        showInfo: true
      },
      onRowUpdating: function (e) {
        e.newData = { ...e.oldData, ...e.newData };
      },
    });

  } catch (error) {
    console.error('Error fetching fighters:', error);
    return;
  }
}
async function buildTeamsManagementDataGrid(container) {

  const teamService = new TeamService(baseUrl);
  const dataGrid = document.createElement('div');
  dataGrid.id = 'teams-management-grid';
  dataGrid.className = 'dx-datagrid';
  container.appendChild(dataGrid);

  try {
    $(dataGrid).dxDataGrid({
      dataSource: createCustomStore(teamService),
      keyExpr: 'id',
      showBorders: true,
      height: 500,

      editing: {
        mode: "popup",
        allowUpdating: true,
        allowAdding: true,
        allowDeleting: true,
        useIcons: true,
        popup: {
          title: "Team",
          showTitle: true,
          width: 600,
          height: 'auto'
        },
        form: {
          items: [
            { dataField: "name", validationRules: [{ type: "required" }] },
            { dataField: "coach_name", validationRules: [{ type: "required" }] },
            { dataField: "country_id", editorType: "dxSelectBox", editorOptions: { dataSource: [], valueExpr: 'id', displayExpr: 'name' }, validationRules: [{ type: "required" }] }
          ]
        }
      },
      columnAutoWidth: true,
      toolbar: {
        items: [
          {
            name: 'addRowButton',
            showText: 'always',
            location: 'after',
            widget: 'dxButton',
            options: {
              icon: 'add',
              text: 'Add Team',
              onClick() {
                $(dataGrid).dxDataGrid('instance').addRow();
              }
            }
          },
          {
            name: 'refreshButton',
            showText: 'always',
            location: 'after',
            widget: 'dxButton',
            options: {
              icon: 'refresh',
              text: 'Refresh',
              onClick() {
                $(dataGrid).dxDataGrid('instance').refresh();
              }
            }
          }
        ]
      },
      columns: [
        { dataField: 'name', caption: 'Team Name' },
        { dataField: 'coach_name', caption: 'Coach Name' },
        { dataField: 'country_id', caption: 'Country', lookup: { dataSource: [], valueExpr: 'id', displayExpr: 'name' } },
        { dataField: 'created_at', caption: 'Created At', dataType: 'date', format:'shortDateShortTime', allowEditing:false, visible:false },
        { dataField:'updated_at', caption:'Updated At', dataType:'date', format:'shortDateShortTime', allowEditing:false, visible:false }
      ],

      paging:{
        pageSize : 10
      },
      pager:{
        showPageSizeSelector:true,
        allowedPageSizes:[5,10,20],
        showInfo:true
      },

      onRowUpdating(e) {
        e.newData = {...e.oldData, ...e.newData};
      }
    });
  } catch (error) {
    console.error('Error fetching teams:', error);
    return;
  }
}

document.addEventListener('DOMContentLoaded', async () => {

  const athleteContainer = document.getElementById('athlete-management');
  const teamsContainer = document.getElementById('teams-management');

  await buildAthleteManagementDataGrid(athleteContainer);
  await buildTeamsManagementDataGrid(teamsContainer);


});